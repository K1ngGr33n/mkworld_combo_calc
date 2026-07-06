import fileIO as fIO
import os
import calcHandler as cH

filePathTimings = "timings.txt" # SINGLE
fileNameResults = "results"
filePathDir = "usedTimings" # MULTIPLE
filePathResults = "allResults"

# calculate everything
calcMultiple = False
logTime = True

if calcMultiple:
    txtFiles = cH.getTxtFiles(filePathDir)
    for e in txtFiles:
        temp = fIO.readTextFile(f"{filePathDir}\\{e}")
        listOfTimings = temp[1]

        try:
            os.makedirs(filePathResults)
        except FileExistsError: # directory already exists
            pass

        cH.runCalcs(listOfTimings, temp[0], e, f"{filePathResults}\\{fileNameResults}.{e}", 0, False, logTime)
else:
    temp = fIO.readTextFile(filePathTimings)
    listOfTimings = temp[1]
    cH.runCalcs(listOfTimings, temp[0], filePathTimings, fileNameResults, 0, False, logTime)