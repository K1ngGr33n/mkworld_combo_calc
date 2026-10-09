import fileIO as fIO
import os
import calcHandler as cH
import time

filePathTimings = "timings.txt" # SINGLE
fileNameResults = "results"
filePathDir = "usedTimings" # MULTIPLE
filePathResults = "allResults"

# calculate everything, keep 
calcMultiple = False
logTime = True

# limits, keep empty to include all
limitC = []
limitV = []

# begin calculation
startTimeFull = time.perf_counter()

if calcMultiple:
    txtFiles = cH.getTxtFiles(filePathDir)
    for e in txtFiles:
        temp = fIO.readTextFile(f"{filePathDir}\\{e}")
        listOfTimings = temp[1]

        try:
            os.makedirs(filePathResults)
        except FileExistsError: # directory already exists
            pass

        cH.runCalcs(listOfTimings, temp[0], [limitC, limitV], e, f"{filePathResults}\\{fileNameResults}.{e}", 0, False, logTime)
else:
    temp = fIO.readTextFile(filePathTimings)
    listOfTimings = temp[1]
    cH.runCalcs(listOfTimings, temp[0], [limitC, limitV], filePathTimings, fileNameResults, 0, False, logTime)

endTimeFull = time.perf_counter()
print(f"Process completed in {endTimeFull-startTimeFull}s")