import timingsCalc as tC
import stats as st
import re

def readTextFile(filePath: str):
    """
    Gets timings from a text file, including the event.
    """
    baseIndex = []

    timingsList = [] # list that gets returned
    section = [] # singular section

    # read timings file, get all sections
    with open(filePath, "r", encoding="utf-8") as tmFile:
        # get base combo values
        tmFile.seek(0)
        baseIndex = tmFile.readline().split()
        
        # separate into sections
        for l in tmFile:
            # get section and add to timingsList
            section = re.split("\s", l.strip())
            section[0] = tC.timeToMils(section[0])
            timingsList.append(section)

    return [baseIndex, timingsList]

def exAsTxtFile(orgFile: str, filepath: str, times, gtTimes):
    # individual GT times
    totalTime = gtTimes[0] + gtTimes[1] + gtTimes[2] + gtTimes[3] + gtTimes[4] + gtTimes[5]
    gts, prct = [], []
    for e in gtTimes:
        gts.append(tC.milsToTime(e))
        prct.append(round(e / totalTime * 100, 2))

    # start of results file
    formattedText = f'''Read from file "{orgFile}"
Road: {gts[0]} ({prct[0]}%) | Terrain: {gts[1]} ({prct[1]}%) | Water: {gts[2]} ({prct[2]}%)
Neutral: {gts[3]} ({prct[3]}%) | Offroad: {gts[4]} ({prct[4]}%) | None: {gts[5]} ({prct[5]}%)
Total Time: {tC.milsToTime(totalTime)}
'''

    for e in times:
        # get names
        n = st.getNames(e[0])

        # write line       [        timestamp         ]   [  char  ]  [  veh  ]
        formattedText += f"\n{tC.milsToTime(e[1])} - {n[0]} / {n[1]}"
    
    with open(f"{filepath}.txt", "w", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        tmFile.write(formattedText)
    print(f'Successfully wrote to "{filepath}.txt"')

# def exAsCsvFile(filepath: str, times):
#     """wip"""