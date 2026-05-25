import timingsCalc as tC
def exAsTxtFile(orgFile: str, filepath: str, times):
    formattedText = f'Read from file "{orgFile}":\n'

    for e in times:
        # write line       [        timestamp         ]   [  char  ]  [  veh  ]
        formattedText += f"\n{tC.milsToTime(round(e[1]))} - {e[0][0]} / {e[0][1]}"
    
    with open(f"{filepath}.txt", "w", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        tmFile.write(formattedText)
    print(f'Successfully wrote to "{filepath}.txr"')

# def exAsCsvFile(filepath: str, times):
#     """wip"""