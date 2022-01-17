'''
This implements the selection sort algorithm.  Selection sort repeatedly
selects the smallest element in the list and puts it into the correct position
in the list.
Parameters:  aList - a list of elements of comparable types.
Output:  None -- aList is sorted in place
'''
def selectionSort(aList):
    for i in range(len(aList)):
        #set minimum value to be the first value in the list
        min = i
        j = min + 1
        #find the index of the minimum value in the list from i+1 to end
        while j < len(aList):
            if aList[j] < aList[min]:
                min = j
            j = j + 1
        if (min != i):
            #swap the values
            aList[min], aList[i] = aList[i], aList[min]
        
 

selectionSort([2,1, 5,7])
        
