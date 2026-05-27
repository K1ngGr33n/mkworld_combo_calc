import resultsExport as rX
import timingsCalc as tC

filePathTimings = "timings.txt"
fileNameResults = "results"

listOfTimings = tC.readTextFile(filePathTimings)

# calculate everything
result = tC.calcLoop(listOfTimings)
trueResult = result[1:]
resultSorted = sorted(trueResult, key=lambda x: x[1]) # sort values

rX.exAsTxtFile(filePathTimings, fileNameResults, resultSorted, result[0])