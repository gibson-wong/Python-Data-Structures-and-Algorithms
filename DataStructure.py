import random

def CreateListOfSize100 ():
    randomList = []
    for i in range(100):
        randomNum = random.randint(1,100)
        randomList.append(randomNum)
    return randomList
a = CreateListOfSize100()


def swap(listA, index1, index2):
    temp = listA[index1]
    listA[index1] = listA[index2]
    listA[index2] = temp
    return listA

#============================Quick Sort====================================
def partition(listA, indexLow, indexHi):
    pivotIndex = random.randint(indexLow, indexHi)
    pivotValue = listA[pivotIndex]
    #swap pivot to last element
    listA=swap(listA, pivotIndex, indexHi)

    #store counter
    indexCounter = indexLow

    #split low and high values
    for i in range (indexLow, indexHi):
         if listA[i] < pivotValue:
            listA = swap(listA, i, indexCounter)
            indexCounter+=1
        
    swap(listA, indexCounter, indexHi)
    return indexCounter

def QuickSort(listOfNum, indexLow, indexHi):
    #base case occurs only when our index crosses path
    if indexLow < indexHi:
        p = partition(listOfNum, indexLow,indexHi)
        QuickSort(listOfNum,indexLow, p-1)
        QuickSort(listOfNum,p+1, indexHi)
              
    return listOfNum


#=========================MIN-HEAP===========================
#Tree represented as a list
#Left node is 2i+1
#Right node is 2i+2
#Parent node is Floor (i-1)/2







