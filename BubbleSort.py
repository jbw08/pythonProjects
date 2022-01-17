def bubbleSort(data):
    print(data)
    swap = True
    end = len(data) - 1
    while swap:
        swap = False
        for i in range (end):
            if data[i] > data[i+1]:
                #if there has been a swap then swap is set to true otherwise its not.
                data[i], data[i+1] = data[i+1], data[i]
                swap = True
        end -= 1
    print(data)

myList = []
bubbleSort(myList)