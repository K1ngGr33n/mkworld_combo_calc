import resultsExport as rX
import timingsCalc as tC

filePathTimings = "timings.txt"
fileNameResults = "results"

listOfTimings = tC.readTextFile(filePathTimings)
print(listOfTimings)

# calculate everything
result = tC.calcLoop(listOfTimings)
resultSorted = sorted(result, key=lambda x: x[1]) # sort values

rX.exAsTxtFile(filePathTimings, fileNameResults, resultSorted)