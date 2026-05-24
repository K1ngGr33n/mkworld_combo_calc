import numpy as np
import pandas as pd
import re

# character/vehicle stats
cStats = []
vStats = []

# end stats/names
tStats = []
tNames = ["", ""]

# stat/coin curve CSVs
csvCharStats = pd.read_csv("csv/charStats.csv")
csvVehStats = pd.read_csv("csv/vehStats.csv")
csvCoinCurve = pd.read_csv("csv/coinCurve.csv")

# test stuff
testInputCombos = [["mario", "blooper"]]

# the rest

def viewStats(combos: str):
    """
    Get the stats of (up to) 10 combos.

    Parameters
    ----------
    combos: str
        Comma separated combos
    """
    fullStats = []

    # get all combos
    inputList = re.split(",+", combos)
    if len(inputList) > 10: # more than 10 combos
        raise OverflowError(f"Too many combos! (received {len(inputList)} combos, only 10 allowed)")
    elif len(inputList) == 0:
        raise IndexError("Please input a combo to show stats!")

    # create list of short names: [["c", "v"], ...]
    for i in range(len(inputList)):
        inputList[i] = str(inputList[i]).strip().lower()

    # process inputs into correct format: [["c", "v"], [0, 0, 0], [1, 2, 3], ...]
    processedList = inputList
    incorrectCombos = ""

    for i in range(len(inputList)):
        if len(re.findall("\\s+", inputList[i])) != 1: # bad syntax
            incorrectCombos = incorrectCombos + ", " if incorrectCombos != "" else "" + str(i+1)
            raise SyntaxError(f"Bad input! (incorrect syntax in these combos: {incorrectCombos})")
        processedList[i] = re.split("\\s+", inputList[i]) # split character/vehicle
    
    # get and assign values
    try:
        fullStats = getNamesAndStats(processedList) # assign values
    except ValueError as e:
        raise ValueError(f"Bad input! ({e})")
    
    return fullStats

def getNamesAndStats(combos):
    returnVal = [[["", ""], [0 for _ in range(10)], [0.0 for _ in range(21)]] for _ in range(len(combos))] # [[["char", "veh"], [stats], [coin curve]], ...]

    for i in range(len(combos)):
        # 
        # character
        #
        row = csvCharStats.index[csvCharStats["Short"] == combos[i][0]].tolist() # find row index
        
        # not found
        if row == []: 
            raise ValueError(f"\"{combos[i][0]}\" is not a character") # error for nonexistent character
        
        result = csvCharStats.iloc[row[0]].tolist() # get row values
        tNames[0] = csvCharStats.at[row[0], "Name"] # get name
        cStats = ["" for _ in range((len(result)-2))] # get only stats
        for k in range(len(result)-2):
            cStats[k] = int(result[k+2])
        
        #
        # vehicle 
        #
        row = csvVehStats.index[csvVehStats["Short"] == combos[i][1]].tolist() # find row index
        
        # not found
        if row == []:     
            raise ValueError(f"\"{combos[i][1]}\" is not a vehicle") # error for nonexistent vehicle
        
        result = csvVehStats.iloc[row[0]].tolist() # get row values
        tNames[1] = csvVehStats.at[row[0], "Name"] # get name
        vStats = ["" for _ in range((len(result)-2))] # get only stats
        for k in range(len(result)-2):
            vStats[k] = int(result[k+2])
        
        tStats = np.add(cStats, vStats).tolist() # total stats

        returnVal[i][0] = [tNames[0], tNames[1]]
        returnVal[i][1] = tStats

        #
        # coins
        #
        for i in range(len(returnVal)):
            result = csvCoinCurve.iloc[returnVal[i][1][6]].tolist() # get row values
            for k in range(len(result)-1):
                returnVal[i][2][k] = float(result[k+1])

        # [[["h", "h"], [1, 1, 1...], [1, 2, 3...]], ...]
        # [combo][names/stats/coin curve][values]
    
    return returnVal