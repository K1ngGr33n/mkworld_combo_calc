def sortTimings(input, mode = 0):
    """
    Sort a list of timings. 
    Mode 0: normal
    Mode 1 or 2: show best vehicle/character
    """
    processList = [[] for _ in range(24)]

    nl = 0
    output = []

    if mode == 0:
        output = sorted(input, key=lambda x: x[1])
    else:
        for e in input:
            processList[e[0][mode-1]].append(e)

        for i in range(0, len(processList)):
            if processList[i-nl] == []:
                processList.pop(i-nl)
                nl += 1

        for n in processList:
            o = sorted(n, key=lambda x: x[1])[0]
            output.append(o)
        output = sorted(output, key=lambda x: x[1])

    return output