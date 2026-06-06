import fileIO as fIO
import timingsCalc as tC
import listSort as lS

filePathTimings = "timings.txt"
fileNameResults = "results"

temp = fIO.readTextFile(filePathTimings)
listOfTimings = temp[1]

# calculate everything
result = tC.calcLoop(listOfTimings, temp[0], False)
trueResult = result[0][1:]
resultSorted = lS.sortTimings(trueResult, 0) # 0: normal, 1: best vehicle, 2: best character

fIO.exAsTxtFile(filePathTimings, fileNameResults, resultSorted, result[1], result[2])