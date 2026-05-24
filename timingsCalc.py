import re

def fileToTimes(filePath: str):
    """
    Gets timings from a text file, including the event.
    """
    timingsList = [] # list that gets returned
    lineCount = 0
    section = [] # singular section

    # read timings file, get all sections
    with open(filePath, "r", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        for l in tmFile:
            # get section and add to timingsList
            section = l.strip().split(" ")
            section[0] = timeToMils(section[0])
            timingsList.append(section)
            
            lineCount += 1

    return timingsList

def timeToMils(inputTime: str):
    """
    Converts a timestamp (M:ss.mmm) to milliseconds.

    Parameters:
    -----------
    inputTime: str
        The timestamp
    """
    ms = 0
    tmStp = re.split(r"[:.]", inputTime)
    
    for i in range(3):
        # 
        tmStp[i] = int(tmStp[i][:i+1].ljust(i+1, "0")) # :3

    return tmStp

def milsToTime(inputTime: int):
    """
    Converts a milliseconds into a timestamp (M:ss.mmm).

    Parameters:
    -----------
    inputTime: int
        The time in milliseconds
    """
    print(inputTime)

