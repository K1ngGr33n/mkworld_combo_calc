import timingsCalc as tC
import stats as st
import re
import matplotlib as mpl

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
            section = re.split(r"\s+", l.strip())
            section[0] = tC.timeToMils(section[0])
            timingsList.append(section)

    return [baseIndex, timingsList]

def exAsTxtFile(orgFile: str, filepath: str, times, gtTimes, calcTime = ""):
    # individual GT times
    totalTime = sum(gtTimes)
    gts, prct = [], []
    for e in gtTimes:
        gts.append(tC.milsToTime(e))
        prct.append(round(e / totalTime * 100, 2))

    # start of results file
    formattedText = f'''Read from file "{orgFile}"
Road: {gts[0]} ({prct[0]}%) | Terrain: {gts[1]} ({prct[1]}%) | Water: {gts[2]} ({prct[2]}%)
Neutral: {gts[3]} ({prct[3]}%) | Offroad: {gts[4]} ({prct[4]}%) | Gliders: {gts[5]} ({prct[5]}%)
None: {gts[6]} ({prct[5]}%)
Total Time: {tC.milsToTime(totalTime)} {f"(finished in {round(calcTime, 4)}s)" if calcTime != "" else ""}
'''

    for e in times:
        # get names
        n = st.getNames(e[0])

        # write line       [        timestamp         ]   [  char  ]  [  veh  ]
        formattedText += f"\n{tC.milsToTime(sum(e[1]))} - {n[0]} / {n[1]}"
    
    with open(f"{filepath}.txt", "w", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        tmFile.write(formattedText)
    print(f'Successfully wrote to "{filepath}.txt"')

def exAsSpeedGraph(orgFile: str, filepath: str, times, combosToUse):
    for e in combosToUse:
        print()

# def exAsCsvFile(filepath: str, times):
#     """wip"""