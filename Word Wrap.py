from array import *

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
    breakWordIndex = []
    print(lineCostLookUp)
    opt[0] = 0
    assignmentIndex[0] = 0
    for i in range(1,size+1):
        min = 99999999
        for j in range(1,i+1):
            temp = opt[j-1] + lineCostLookUp[j-1][i-1]
            if(temp < min):
                min = temp
        opt[i] = min
    return opt

if __name__ == '__main__':
    sample = "Who is it"
    lineWidth = 6
    lineCostLookUp = prepareLineCostTable(sample,lineWidth)
    #print(lineCostLookUp)
    assignment = getWrappedTextAssignment(lineCostLookUp)
    print(assignment)