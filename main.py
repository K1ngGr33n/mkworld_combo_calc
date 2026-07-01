import fileIO as fIO
import timingsCalc as tC
import listSort as lS
import os
import os.path as op
import re 
import calcHandler as cH

filePathTimings = "timings.txt"
fileNameResults = "results"
filePathDir = "usedTimings"
filePathResults = "allResults"

# calculate everything
calcMultiple = False

if calcMultiple:
    txtFiles = cH.getTxtFiles(filePathDir)
    for e in txtFiles:
        temp = fIO.readTextFile(f"{filePathDir}\\{e}")
        listOfTimings = temp[1]

        try:
            os.makedirs(filePathResults)
        except FileExistsError: # directory already exists
            pass

        cH.runCalcs(listOfTimings, temp[0], e, f"{filePathResults}\\{fileNameResults}.{e}", 0, False, False)
else:
    temp = fIO.readTextFile(filePathTimings)
    listOfTimings = temp[1]
    cH.runCalcs(listOfTimings, temp[0], filePathTimings, fileNameResults, 0, False, False)