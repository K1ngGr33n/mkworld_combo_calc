import re

# stat/coin curve CSVs
csvCharStats = open("csv/charStats.csv", "r", encoding="utf-8") # Name,Index,RS,TS,WS,GS,AC,MT,CC
csvVehStats = open("csv/vehStats.csv", "r", encoding="utf-8") # Name,Index,RS,TS,WS,GS,AC,MT,CC
csvCoinCurve = open("csv/coinCurve.csv", "r", encoding="utf-8") # S/C,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

# test stuff
testInputCombo = [7, 10]

# the rest

def getNames(pos: int):
    returnVal = ["", ""] # ["char", "veh"]
    # 
    # character
    #
    current = []
    csvCharStats.seek(0)
    for e in csvCharStats:
        current = list(filter(None, re.split(r"[,\n]", e))) # convert line in csv file to list
        if current[1] == str(pos[0]): # check against given index
            returnVal[0] = current[0]
            break

    # 
    # vehicle
    #
    current = []
    csvVehStats.seek(0)
    for e in csvVehStats:
        current = list(filter(None, re.split(r"[,\n]", e))) # convert line in csv file to list
        if current[1] == str(pos[1]): # check against given index
            returnVal[1] = current[0]
            break
    
    return returnVal

def getStats(pos: int):
    returnVal = [0, 0] # [[stats], [coin curve]]
    # 
    # character
    #
    csvCharStats.seek(0)
    for e in csvCharStats:
        current = list(filter(None, re.split(r"[,\n]", e))) # convert line in csv file to list
        if current[1] == str(pos[0]): # check against given index
            for i in range(len(current)-2): # convert numbers to int
                current[i+2] = int(current[i+2])
            returnVal[0] = current[2:]
            break

    # 
    # vehicle
    #
    csvVehStats.seek(0)
    for e in csvVehStats:
        current = list(filter(None, re.split(r"[,\n]", e))) # convert line in csv file to list
        if current[1] == str(pos[1]): # check against given index
            for i in range(len(current)-2): # convert numbers to int
                current[i+2] = int(current[i+2])
            for i in range(len(returnVal[0])): # add stats onto character stats
                    returnVal[0][i] += current[i+2]
            break

    #
    # coins
    #
    csvCoinCurve.seek(0)
    for e in csvCoinCurve:
            current = list(filter(None, re.split(r"[,\n]", e))) # convert line in csv file to list
            if current[0] == str(returnVal[0][6]): # check against given index
                for i in range(len(current)-1): # convert numbers to int
                    current[i+1] = float(current[i+1])
                    returnVal[1] = current[1:]
                break

    return returnVal

# print(f"{getStats(testInputCombo)}\n{getNames(testInputCombo)}")