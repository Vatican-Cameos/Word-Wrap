
def prepareLineCostTable(sample, lineWidth):
    print("Preparing Line Costs")
    lineCost = [[0 for x in range(len(sample.split(" ")))] for y in range(len(sample.split(" ")))]

    for i,word in enumerate(sample.split(" ")):
        lengthI = len(word)
        lengthJ = 0
        #print(sample.split(" ")[i:])
        j = i
        for wordJ in enumerate(sample.split(" ")[i:]):
            #print("i : " +str(i)+ " j :" + str(j))
            if(j == i):
                lengthJ = lengthI
            else:
                lengthJ = lengthJ + len(wordJ) + 1
            #print("\nlength " + str(lengthJ))

            if lengthJ <= lineWidth:
                lineCost[i][j] = lineWidth - lengthJ
            else:
                lineCost[i][j] = 99999999999
            j += 1

    return lineCost

def getWrappedTextAssignment(lineCostLookUp):
    print("Cooking text")
    size = len(sample.split(" "))
    opt = [0] * (size + 1)
    assignmentIndex = [0] * (size + 1)
    resultIndex = [0] * (size + 1)
    #print(lineCostLookUp)
    opt[0] = 0
    assignmentIndex[0] = 0
    resultIndex[0] = 0
    for i in range(1,size+1):
        min = 99999999
        for j in range(1,i+1):
            temp = opt[j-1] + lineCostLookUp[j-1][i-1]
            if(temp < min):
                min = temp
                resultIndex[i] = j-1
        opt[i] = min
        print(opt)
    return resultIndex

if __name__ == '__main__':
    File_object = open(r"test.txt", "r")
    sample = File_object.read()
    File_object.close()
    print(sample)
    #sample = "Who is it and what are you"

    lineWidth = 15
    lineCostLookUp = prepareLineCostTable(sample,lineWidth)
    #print(lineCostLookUp)
    assignment = getWrappedTextAssignment(lineCostLookUp)
    result = [0] * (len(assignment))
    for i in range(1,len(assignment)):
        result[i] = result[assignment[i]] + 1

    lineNo = 1
    stringNew = ''
    index = 1

    for word in sample.split():
        wordIndex = result[index]
        if(lineNo == wordIndex):
            stringNew += word + ' '
        else:
            lineNo = result[index]
            stringNew += '\n' + word + ' '
        index += 1

    print(stringNew)
    File_object = open(r"formatted.txt", "w")
    File_object.write(stringNew)
    File_object.close()
    print(result)


def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]