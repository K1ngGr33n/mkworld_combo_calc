import re
import stats as st
import time

def timeToMils(inputTime: str):
    """
    Converts a timestamp (M:ss.mmm) to milliseconds.

    Parameters:
    -----------
    inputTime: str
        The timestamp
    """
    ms = 0.0
    tmStp = re.split(r"[:.]", inputTime)
    
    for i in range(3):
        # converts times (M:ss:mmm) to integers
        tmStp[i] = int(tmStp[i][:i+1].ljust(i+1, "0")) # :3

    # add everything together and return
    ms = float(tmStp[0]*60000 + tmStp[1]*1000 + tmStp[2])
    return ms

def milsToTime(inputTime: int):
    """
    Converts a milliseconds into a timestamp (M:ss.mmm).

    Parameters:
    -----------
    inputTime: int
        The time in milliseconds
    """
    inputTime = int(round(inputTime))

    mins = str(inputTime // 60000)
    secs = str((inputTime % 60000) // 1000)[:2].rjust(2, "0")
    mils = str(inputTime % 1000)[:3].rjust(3, "0")
    
    timestamp = f"{mins}:{secs}.{mils}"

    return timestamp

# def calcTimeDiff(baseSpeed, timings, newStats: int):
#     """
#     Calculates the time difference between 2 combos in one specific section.

#     Parameters:
#     -----------
#     baseTime: float
#         The time from the baseline run.
    
#     newCombo: int
#         The combo to compare against. [char index, veh index]
    
#     groundType: str
#     coinCount: int
#         Self explanatory.
#     """
    

#     return

def calcSectSpeed(timings, stats):
    gts = ["r", "t", "w", "n", "o", "x"]
    speedList = []

    boost = 0
    coinCount = 0

    speed = 100.0
    for e in timings:
        if e[1].lower() == "c":
            coinCount += 1
        else:
            pos = gts.index(e[1].lower())
        if pos < 3: # road/terrain/water
            speed = (100 + (0.312 * stats[0][pos])) * (1 + stats[1][coinCount]/100) * (1 + boost/100)
        elif pos < 5: # neutral/offroad
            speed = 100 * (1 + stats[1][coinCount]/100) * (1 + boost/100)
        else: # none
            speed = 100

        speedList.append(speed)

    return speedList

def calcBaseSections(timings: int):
    sect, gtTimes = [], [0, 0, 0, 0, 0, 0]
    gts = ["r", "t", "w", "n", "o", "x"]
    coins = 0

    for i in range(len(timings)-1):
        # calculate time differences
        if timings[i][1].lower() == "c":
            coins += 1
        else:
            groundType = timings[i][1]
        
        diff = timings[i+1][0]-timings[i][0]
        sect.append([diff, timings[i][1]])
        
        # calculate total time for each ground type
        pos = gts.index(groundType.lower())
        if pos < 3 or pos == 5: # gt is r, t, w, or x
            gtTimes[pos] += diff
        elif pos < 5: # gt is n or o
            if coins != 0 and coins != 20:
                gtTimes[pos] += diff
            else: 
                gtTimes[5] += diff

    return [sect, gtTimes]

def calcLoop(timings, baseCombo: int, calcLog = False, speedLog = False):
    """
    Loops through all combos
    """
    finalTimes = []

    # get base stats
    baseStats, newStats = st.getStats(baseCombo), []

    limitC, limitV = [], []

    gtTimes = [0, 0, 0, 0, 0, 0]
    x = 0

    # begin calculation
    startTime = time.perf_counter()

    # get base combo values
    temp = calcBaseSections(timings)
    baseSections = temp[0]
    gtTimes = temp[1]
    baseSpeed = calcSectSpeed(baseSections, baseStats)

    #speedList = [[[]]]

    # calculate every combo
    for c in limitC if limitC != [] else range(20): # loop characters
        for v in limitV if limitV != [] else range(24): # loop vehicles
            newStats = st.getStats([c, v])
            newSpeed = calcSectSpeed(baseSections, newStats)
            newTime = 0.0
            
            # calculate new time
            for i in range(len(baseSections)):
                newTime += (baseSpeed[i] * baseSections[i][0]) / newSpeed[i]

            finalTimes.append([[c, v], newTime]) # add to list

            if calcLog:
                x += 1
                cN = st.getNames([c, v])
                print(f"Calculated {x}/{(len(limitC) * len(limitV) if limitC != [] and limitV != [] else 480)} ({cN[0]} / {cN[1]})")
            
            #if speedLog:
                #speedList[c][v].append(newSpeed)

    endTime = time.perf_counter()

    print(f"Calculation done ({endTime - startTime}s)")
    return [finalTimes, gtTimes, endTime - startTime]#, speedList]

# print(milsToTime(65369.0 + 0 + 35843.0 + 27726.0 + 238.0 + 128.0))