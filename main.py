import resultsExport as rX
import timingsCalc as tC
import listSort as lS

filePathTimings = "timings.txt"
fileNameResults = "results"

listOfTimings = tC.readTextFile(filePathTimings)

# calculate everything
result = tC.calcLoop(listOfTimings)
trueResult = result[1:]
resultSorted = lS.sortTimings(trueResult, 0) # 0: normal, 1: best vehicle, 2: best character

rX.exAsTxtFile(filePathTimings, fileNameResults, resultSorted, result[0])