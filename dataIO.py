import calcHandler as cH
import stats as st
import re, os
# import matplotlib as mpl

def getTxtFiles(tPath: str):
    return [f for f in os.listdir(tPath) if re.split(r"[.]", f)[-1] == "txt"]

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
            if l.strip()[0] != "#": # skip line if comment
                section = re.split(r"\s+", l.strip())
                section[0] = cH.timeToMils(section[0])
                timingsList.append(section)
                if section[1] == "e": # exit if run end ("e") is found
                    break

    return [baseIndex, timingsList]

def sortResults(input, mode = 0):
    """
    Sort a list of results. 
    Mode 0: normal
    Mode 1 or 2: show best vehicle/character
    """
    processList = [[] for _ in range(24)]

    nl = 0
    output = []

    if mode == 0:
        output = sorted(input, key=lambda x: sum(x[1]))
    else:
        for e in input:
            processList[e[0][mode-1]].append(e)

        for i in range(0, len(processList)):
            if processList[i-nl] == []:
                processList.pop(i-nl)
                nl += 1

        for n in processList:
            o = sorted(n, key=lambda x: x[1])[0]
            output.append(o)
        output = sorted(output, key=lambda x: x[1])

    return output

def exAsTxtFile(orgFile: str, filepath: str, times, gtTimes, calcTime):
    # individual GT times
    totalTime = sum(gtTimes)
    gts, prct = [], []
    for e in gtTimes:
        gts.append(cH.milsToTime(e))
        prct.append(round(e / totalTime * 100, 2))

    # start of results file
    formattedText = f'''Read from file "{orgFile}"
Road: {gts[0]} ({prct[0]}%) | Terrain: {gts[1]} ({prct[1]}%) | Water: {gts[2]} ({prct[2]}%)
Neutral: {gts[3]} ({prct[3]}%) | Offroad: {gts[4]} ({prct[4]}%) | Gliders: {gts[5]} ({prct[5]}%)
None: {gts[6]} ({prct[5]}%)
Total Time: {cH.milsToTime(totalTime)} {f"(finished in {round(calcTime, 4)}s)" if calcTime != "" else ""}
'''

    for e in times:
        # get names
        n = st.getNames(e[0])

        # write line       [        timestamp         ]   [  char  ]  [  veh  ]
        formattedText += f"\n{cH.milsToTime(sum(e[1]))} - {n[0]} / {n[1]}"
    
    with open(f"{filepath}.txt", "w", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        tmFile.write(formattedText)
    print(f'Results written to "{filepath}.txt"')

# def exAsSpeedGraph(orgFile: str, filepath: str, times, combosToUse):
#     """wip maybe"""
#     for e in combosToUse:
#         print()

# def exAsCsvFile(filepath: str, times):
#     """wip"""