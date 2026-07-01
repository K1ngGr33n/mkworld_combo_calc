import os
import re 
import fileIO as fIO
import timingsCalc as tC
import listSort as lS

def getTxtFiles(tPath: str):
    return [f for f in os.listdir(tPath) if re.split(r"[.]", f)[-1] == "txt"]

def runCalcs(listOfTimings, baseCombo: int, tFileName: str, rFileName: str, mode = 0, calcLog = False, speedLog = False):
    result = tC.calcLoop(listOfTimings, baseCombo, calcLog, speedLog)
    trueResult = result[0][1:]
    resultSorted = lS.sortTimings(trueResult, mode) # 0: normal, 1: best vehicle, 2: best character

    fIO.exAsTxtFile(tFileName, rFileName, resultSorted, result[1], result[2])