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

def calcTimeDiff(baseStats: int, baseTime: float, newStats: int, groundType: str, coinCount: int, boost = 0):
    """
    Calculates the time difference between 2 combos in one specific section.

    Parameters:
    -----------
    baseTime: float
        The time from the baseline run.
    
    newCombo: int
        The combo to compare against. [char index, veh index]
    
    groundType: str
    coinCount: int
        Self explanatory.
    """

    gts = ["r", "t", "w", "n", "o", "x"]
    pos = gts.index(groundType)

    newSpeed = 100.0

    if pos < 3: # road/terrain/water
        newSpeed = (100 + (0.312 * newStats[0][pos])) * (1 + newStats[1][coinCount]/100) * (1 + boost/100)
        baseSpeed = (100 + (0.312 * baseStats[0][pos])) * (1 + baseStats[1][coinCount]/100) * (1 + boost/100)
    elif pos < 5: # neutral/offroad
        newSpeed = 100 * (1 + newStats[1][coinCount]/100) * (1 + boost/100)
        baseSpeed = 100 * (1 + baseStats[1][coinCount]/100) * (1 + boost/100)
    else: # none
        return baseTime

    # calculate new time
    newTime = (baseSpeed * baseTime) / newSpeed

    return newTime

def calcLoop(timings, baseCombo: int, log = False):
    """
    Loops through all combos
    """
    finalTimes = []

    sectionTimeBase, sectionTimeNew, totalTimeNew, coins = 0.0, 0.0, 0.0, 0
    groundType = ""

    # get base stats
    baseStats, newStats = st.getStats(baseCombo), []

    limitC, limitV = [], []

    baseTimesDone = False

    gts = ["r", "t", "w", "n", "o", "x"]
    gtTimes = [0, 0, 0, 0, 0, 0]

    startTime = time.perf_counter()
    for c in limitC if limitC != [] else range(20): # loop characters
        for v in limitV if limitV != [] else range(24): # loop vehicles
            newStats = st.getStats([c, v])

            for s in range(len(timings)-1): # loop through sections
                if timings[s][1] != "e": # loop has not reached end

                    # calculate base time in section
                    sectionTimeBase = timings[s+1][0] - timings[s][0] 
                    if timings[s][1].lower() == "c" and coins < 20: # coin collection
                        coins += 1
                    else: # no coin collection: switch gt
                        groundType = timings[s][1]

                    # measure total amount of each ground type
                    if baseTimesDone == False:
                        pos = gts.index(groundType.lower())
                        if pos < 3 or pos == 5: # gt is r, t, w, or x
                            gtTimes[pos] += sectionTimeBase
                        elif pos < 5: # gt is n or o
                            if coins != 0 and coins != 20:
                                gtTimes[pos] += sectionTimeBase
                            else: 
                                gtTimes[5] += sectionTimeBase
                    
                    # calculate new section time + total time
                    sectionTimeNew = calcTimeDiff(baseStats, sectionTimeBase, newStats, groundType.lower(), coins) 
                    totalTimeNew += sectionTimeNew

            if baseTimesDone == False:
                finalTimes.append(gtTimes)
                baseTimesDone = True

            finalTimes.append([[c, v], totalTimeNew]) # add to list

            # reset variables
            totalTimeNew = 0
            coins = 0
            
            cN = st.getNames([c, v])
            if log:
                print(f"Calculated {(c)*24 + (v+1)}/{(len(limitC) * len(limitV) if limitC != [] and limitV != [] else 480)} ({cN[0]} / {cN[1]})")

    endTime = time.perf_counter()

    print(f"Calculation done ({endTime - startTime}s)")
    return finalTimes

# print(milsToTime(65369.0 + 0 + 35843.0 + 27726.0 + 238.0 + 128.0))