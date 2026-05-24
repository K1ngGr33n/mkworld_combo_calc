import numpy as np
import pandas as pd
import re

# character/vehicle stats
cStats = []
vStats = []

# end stats/names
tNames = ["", ""]

# stat/coin curve CSVs
csvCharStats = pd.read_csv("csv/charStats.csv")
csvVehStats = pd.read_csv("csv/vehStats.csv")
csvCoinCurve = pd.read_csv("csv/coinCurve.csv")

# test stuff
testInputCombo = [7, 10]

# the rest

def viewStats(index: str, coinCount: int):
    """
    Get the stats and coin curve boost of a combo.

    Parameters
    ----------
    index: str
        Combo index
    """
    fullValues = []
    
    # get and assign values
    try:
        fullValues = getNamesAndStats(index, coinCount) # assign values
    except ValueError as e:
        raise ValueError(f"Bad input! ({e})")
    
    return fullValues

def getNamesAndStats(index: int):
    returnVal = [["", ""], [0 for _ in range(10)], [0.0 for _ in range(21)]] # [["char", "veh"], [stats], [coin curve]]

    # 
    # character
    #
    row = csvCharStats.index[csvCharStats["Index"] == int(index[0])].tolist()[0] # find row index
    
    # not found
    if row == []: 
        raise ValueError(f"\"{index[0]}\" is not a character") # error for nonexistent character
    
    result = csvCharStats.iloc[row].tolist()[3:] # get row values
    tNames[0] = csvCharStats.at[row, "Name"] # get name
    cStats = ["" for _ in range((len(result)))] # get only stats
    for k in range(len(result)):
        cStats[k] = int(result[k])
    
    #
    # vehicle 
    #
    row = csvVehStats.index[csvVehStats["Index"] == int(index[1])].tolist()[0] # find row index
    
    # not found
    if row == []: 
        raise ValueError(f"\"{index[0]}\" is not a vehicle") # error for nonexistent character
    
    result = csvVehStats.iloc[row].tolist()[3:] # get row values
    tNames[1] = csvVehStats.at[row, "Name"] # get name
    vStats = ["" for _ in range((len(result)))] # get only stats
    for k in range(len(result)):
        vStats[k] = int(result[k])
    
    returnVal[0] = tNames
    returnVal[1] = np.add(cStats, vStats).tolist()

    #
    # coins
    #
    result = csvCoinCurve.iloc[returnVal[1][5]].tolist()[1:] # get row values
    for k in range(len(result)):
        returnVal[2][k] = float(result[k])

    # [["h", "h"], [1, 1, 1...], [1, 2, 3...]]
    # [names/stats/coin curve]

    return returnVal

def getNames(index: int):
    returnVal = ["", ""] # ["char", "veh"]
    # 
    # character
    #
    row = csvCharStats.index[csvCharStats["Index"] == int(index[0])].tolist()[0] # find row index
    returnVal[0] = csvCharStats.at[row, "Name"]

    # 
    # vehicle
    #
    row = csvVehStats.index[csvVehStats["Index"] == int(index[1])].tolist()[0] # find row index
    returnVal[1] = csvVehStats.at[row, "Name"]
    
    return returnVal

def getStats(index: int):
    returnVal = [[0 for _ in range(10)], [0.0 for _ in range(21)]] # [[stats], [coin curve]]
    # 
    # character
    #
    row = csvCharStats.index[csvCharStats["Index"] == int(index[0])].tolist()[0] # find row index

    result = csvCharStats.iloc[row].tolist()[3:] # get row values
    cStats = ["" for _ in range((len(result)))] # get only stats
    for k in range(len(result)):
        cStats[k] = int(result[k])
    
    # 
    # vehicle
    #
    row = csvVehStats.index[csvVehStats["Index"] == int(index[1])].tolist()[0] # find row index

    result = csvVehStats.iloc[row].tolist()[3:] # get row values
    vStats = ["" for _ in range((len(result)))] # get only stats
    for k in range(len(result)):
        vStats[k] = int(result[k])

    returnVal[0] = np.add(cStats, vStats).tolist()

    #
    # coins
    #
    result = csvCoinCurve.iloc[returnVal[0][5]].tolist()[1:] # get row values
    for k in range(len(result)):
        returnVal[1][k] = float(result[k])

    return returnVal

# print(getStats(testInputCombo))