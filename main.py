import os
import timingsCalc as tC

filePathTimings = "timings.txt"
fileNameResults = "results.txt"

listOfTimings = tC.readTextFile(filePathTimings)
print(listOfTimings)

result = tC.calcLoop(listOfTimings)

resultSorted = sorted(result, key=lambda x: x[1])

with open(fileNameResults, 'w', encoding='utf-8') as file:
    file.write(str(resultSorted))
print(f"Successfully wrote to '{fileNameResults}'.")