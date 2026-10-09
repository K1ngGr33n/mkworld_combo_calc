import os
import re 
import fileIO as fIO
import timingsCalc as tC
import listSort as lS
import time

def getTxtFiles(tPath: str):
    return [f for f in os.listdir(tPath) if re.split(r"[.]", f)[-1] == "txt"]

def runCalcs(listOfTimings, baseCombo: int, limits, tFileName: str, rFileName: str, mode = 0, calcLog = False, timeLog = False):
    if timeLog: startTime = time.perf_counter()
    result = tC.calcLoop(listOfTimings, baseCombo, limits, calcLog)
    trueResult = result[0][1:]
    resultSorted = lS.sortTimings(trueResult, mode) # 0: normal, 1: best vehicle, 2: best character

    if timeLog: endTime = time.perf_counter()
    fIO.exAsTxtFile(tFileName, rFileName, resultSorted, result[1], endTime - startTime if timeLog else "")