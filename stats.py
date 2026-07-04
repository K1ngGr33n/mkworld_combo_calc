import numpy as np
import pandas as pd

# stat/coin curve CSVs
csvCharStats = pd.read_csv("csv/charStats.csv")
csvVehStats = pd.read_csv("csv/vehStats.csv")
csvCoinCurve = pd.read_csv("csv/coinCurve.csv")

# test stuff
testInputCombo = [7, 10]

# the rest

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
    returnVal = [] # [[stats], [coin curve]]
    # 
    # character
    #
    row = csvCharStats.index[csvCharStats["Index"] == int(index[0])].tolist()[0] # find row index

    result = csvCharStats.iloc[row].tolist()[2:] # get row values
    cStats = [] # get only stats
    for k in result:
        cStats.append(int(k))
    
    # 
    # vehicle
    #
    row = csvVehStats.index[csvVehStats["Index"] == int(index[1])].tolist()[0] # find row index

    result = csvVehStats.iloc[row].tolist()[2:] # get row values
    vStats = [] # get only stats
    for k in result:
        vStats.append(int(k))

    returnVal.append(np.add(cStats, vStats).tolist())

    #
    # coins
    #
    result = csvCoinCurve.iloc[returnVal[0][6]].tolist()[1:] # get row values
    returnVal.append(result)

    return returnVal

print(getStats(testInputCombo))