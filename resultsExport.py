import timingsCalc as tC
def exAsTxtFile(orgFile: str, filepath: str, times, gtTimes):
    formattedText = f'''Read from file "{orgFile}":\n'''
# Road: {tC.milsToTime(gtTimes[0])} | Terrain: {tC.milsToTime(gtTimes[1])} | Water: {tC.milsToTime(gtTimes[2])}
# Neutral: {tC.milsToTime(gtTimes[3])} | Offroad: {tC.milsToTime(gtTimes[4])} | None: {tC.milsToTime(gtTimes[5])}
# Total Time: {tC.milsToTime(gtTimes[0] + gtTimes[1] + gtTimes[2] + gtTimes[3] + gtTimes[4] + gtTimes[5])}
# '''

    for e in times:
        # write line       [        timestamp         ]   [  char  ]  [  veh  ]
        formattedText += f"\n{tC.milsToTime(e[1])} - {e[0][0]} / {e[0][1]}"
    
    with open(f"{filepath}.txt", "w", encoding="utf-8") as tmFile:
        tmFile.seek(0)
        tmFile.write(formattedText)
    print(f'Successfully wrote to "{filepath}.txt"')

# def exAsCsvFile(filepath: str, times):
#     """wip"""