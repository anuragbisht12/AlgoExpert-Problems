"""
O(NlogN) time and O(NlogN) space
Less optimized 
"""

def mergeSort(array):
    if len(array)==1:
        return array
    middleIndex=len(array)//2
    leftHalf=array[:middleIndex]
    rightHalf=array[middleIndex:]

    return mergeSortedArrays(mergeSort(leftHalf),mergeSort(rightHalf))

def mergeSortedArrays(leftHalf,rightHalf):
    sortedArray=[None] * (len(leftHalf)+len(rightHalf))
    k=i=j=0
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i]<=rightHalf[j]:
            sortedArray[k]=leftHalf[i]
            i+=1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k+=1
    
    while i<len(leftHalf):
        sortedArray[k]=leftHalf[i]
        i+=1
        k+=1
    
    while j<len(rightHalf):
        sortedArray[k]=rightHalf[j]
        j+=1
        k+=1

    return sortedArray


