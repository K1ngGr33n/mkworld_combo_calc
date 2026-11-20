import stats as st
import dataIO as dIO
import time, re

# stat scalings
#         TST,    TSG,    TSW,    TSG,    TSD,    TSRS,   TSWR,   CSR
#         RS      TS      WS      GS      OS      RaS     WaS     CC
srBase = [0.9670, 0.9700, 0.9400, 0.9500, 1.0000, 0.9500, 0.9500, 0.5000]
srScal = [0.0030, 0.0030, 0.0060, 0.0050, 0.0000, 0.0050, 0.0050, 0.0500]

def runCalcs(listOfTimings, baseCombo: int, limits, tFileName: str, rFileName: str, mode = 0, calcLog = False, timeLog = False):
    if timeLog: startTime = time.perf_counter()
    result = calcLoop(listOfTimings, baseCombo, limits, calcLog)
    trueResult = result[0][1:]
    resultSorted = dIO.sortResults(trueResult, mode) # 0: normal, 1: best vehicle, 2: best character

    if timeLog: endTime = time.perf_counter()
    dIO.exAsTxtFile(tFileName, rFileName, resultSorted, result[1], endTime - startTime if timeLog else "")

# convert a timestamp to milliseconds
def timeToMils(inputTime: str):
    ms = 0.0
    tmStp = re.split(r"[:.]", inputTime)
    
    for i in range(3):
        # converts times (M:ss:mmm) to integers
        tmStp[i] = int(tmStp[i][:i+1].ljust(i+1, "0")) # :3

    # add everything together and return
    ms = float(tmStp[0]*60000 + tmStp[1]*1000 + tmStp[2])
    return ms

# convert milliseconds to a timestamp
def milsToTime(inputTime: int):
    inputTime = int(round(inputTime))

    mins = str(inputTime // 60000)
    secs = str((inputTime % 60000) // 1000)[:2].rjust(2, "0")
    mils = str(inputTime % 1000)[:3].rjust(3, "0")
    
    timestamp = f"{mins}:{secs}.{mils}"

    return timestamp

# calculates the speed for each section
def calcSectSpeed(timings, stats):
    #      TST, TSG, TSW, TSG, TSD, TSRS,TSWR
    #      RS   TS   WS   GS   OS   RaS  WaS  
    gts = ["r", "t", "w", "g", "o", "rl", "wl", "x"]
    speedList = []
    pos = 0

    coinCount = 0

    speed = 1
    for e in timings:
        # section is a coin grab 
        if e[1].lower() == "c":
            if coinCount < 20: 
                coinCount += 1
        # section is an item or shock hit
        elif e[1].lower() == "h" or e[1].lower() == "sh": 
            coinCount -= 3 if e[1].lower() == "h" else 2 
            if coinCount < 0:
                coinCount = 0
        # TST,TSG,TSW,TSG,TSD,TSRS,TSWR,CSR
        else:
            pos = gts.index(e[1].lower())
        
        if pos < 7: # road, terrain, water, glider, offroad, rail or wall
            speed = (srBase[pos] + srScal[pos] * stats[0][pos]) * (1 + stats[1][coinCount]/100)
        #   speed = base Speed   + scaling     * level          * coin buff
        else: # none
            speed = 1
        speedList.append(speed)

    return speedList

# calculates the time of each section from the base run
def calcBaseSections(timings: int):
    sect, gtTimes = [], [0, 0, 0, 0, 0, 0, 0, 0]
    gts = ["r", "t", "w", "g", "o", "rl", "wl", "x"]
    coins = 0
    groundType = "r"

    for i in range(len(timings)-1):
        # calculate time differences
        if timings[i][1].lower() == "c":
            coins += 1
        elif timings[i][1].lower() == "h" or timings[i][1].lower() == "sh":
            coins -= 3 if timings[i][1].lower() == "h" else 2
            if coins < 0:
                coins = 0
        else:
            groundType = timings[i][1]
        
        diff = timings[i+1][0]-timings[i][0]
        sect.append([diff, timings[i][1]])
        
        # calculate total time for each ground type
        if groundType.lower() in gts:
            pos = gts.index(groundType.lower())
        else: # ground type tag is not on the list
            print(f'Error: "{groundType}" is not a valid tag! Please check your timings file.')
            exit()
        gtTimes[pos] += diff

    return [sect, gtTimes]

# loops through all combos and calculates their time
def calcLoop(timings, baseCombo: int, limits, calcLog = False, timeLog = False):
    """
    Loops through all combos
    """
    finalTimes = []

    # get base stats
    baseStats, newStats = st.getStats(baseCombo), []

    gtTimes = [0, 0, 0, 0, 0, 0, 0]
    x = 0

    # begin calculation

    # get base combo values
    temp = calcBaseSections(timings)
    baseSections = temp[0]
    gtTimes = temp[1]
    baseSpeed = calcSectSpeed(baseSections, baseStats)

    # speedList = [[[]]]

    # calculate every combo
    for c in limits[0] if limits[0] != [] else range(20): # loop characters
        for v in limits[1] if limits[1] != [] else range(24): # loop vehicles
            newStats = st.getStats([c, v])
            newSpeed = calcSectSpeed(baseSections, newStats)
            newTimes = []
            
            # calculate new time
            for i in range(len(baseSections)):
                newTimes.append((baseSpeed[i] * baseSections[i][0]) / newSpeed[i])

            finalTimes.append([[c, v], newTimes]) # add to list

            if calcLog:
                x += 1
                cN = st.getNames([c, v])
                print(f"Calculated {x}/{(len(limits[0]) * len(limits[1]) if limits[0] != [] and limits[1] != [] else 480)} ({cN[0]} / {cN[1]})")
            
            #if speedLog:
                #speedList[c][v].append(newSpeed)

    return [finalTimes, gtTimes]#, speedList]

# print(milsToTime(65369.0 + 0 + 35843.0 + 27726.0 + 238.0 + 128.0))