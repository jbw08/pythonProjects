"""
Joshua Blake-Williams
Searching and Sorting
"""
import urllib.request    


def readHtml():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/data121.txt")
    html = response.readline()
    data = []
    while len(html) != 0:
        line = html.decode('utf-8').split()
        data.append(line)
        html = response.readline()

        for x in range (0,len(data)):
            for i in range (1,2):
                data[x][i] = float(data[x][i])
        for x in range (0, len(data)):
            for i in range (0,1):
               data[x][i] = int(data[x][i])
        for x in range (0, len(data)):
            for i in range (2,3):
                data[x][i] = int(data[x][i])

    return data

#print(readHtml())
#Price list created to allow for use in another function
def prices_list (data):
    new_list = []
    for i in range (len(data)):
        for x in range (len(data[i])):
            new_list.append(data[i][1])
    return new_list

def bubbleSort(data):
    #print (data)
    swap = True
    end = len(data) - 1
    while swap:
        swap = False
        for i in range (0, end):
            if data[i] > data[i+1]:
                #if there has been a swap then swap is set to true and a swap occurs, otherwise it does not occur
                data[i], data[i+1] = data[i+1], data[i]
                swap = True
        end -= 1
    data.reverse()
    return(data)

#print(arrangePrices(prices_list(readHtml())))
def duplicate_removal(data):
    end = len(data)-1
    while end > 0:
        if data[end] == data[end - 1]:
            data.pop(end)
        end -= 1
    return data
#print(duplicate_removal(bubbleSort(prices_list(readHtml()))))

#def most_expensive_5(data1,data2):
 #   for x in range (len())
#print(most_expensive_5(duplicate_removal(bubbleSort(prices_list(readHtml()))), readHtml()))
def leastNumUnits(data):
    items_least = []
    index = 0
    i = data[1][2]
    for x in range (len(data)):
        if i > data[x][2]:
            i = data[x][2]
            index = x

    for x in range (len(data)):
        if i == data[x][2]:
            items_least.append(data[x])
    print("The item ID is:",items_least[0][0])
    print("The item Price is: $",items_least[0][1])
    print("The item stock is:",items_least[0][2])
    print("The item ID is:",items_least[1][0])
    print("The item price is: $",items_least[1][1])
    print("The item stock is:",items_least[1][2])
    print("The item ID is:",items_least[2][0])
    print("The item price is: $",items_least[2][1])
    print("The item stock is:",items_least[2][2])
    print("The item ID is:",items_least[3][0])
    print("The item price is: $",items_least[3][1])
    print("The item stock is:",items_least[3][2])
    print("The item ID is:",items_least[4][0])
    print("The item price is: $",items_least[4][1])
    print("The item stock is:",items_least[4][2])
#(leastNumUnits(readHtml()))
def partId(data):
    user_response = int(input("Enter the PartID you wish to see information about: "))
    for x in range (len(data)):
        for i in range (3):
            if user_response == data[x][i]:
                print("The item ID is:",data[x][i],"The number of units available are:",data[x][i+2],"The price of the item chosen is: $",data[x][i+1])
                exit()
            else:
                print("Sorry, item is not available.")
                exit()
#partId(readHtml())

def between5_10(data):
    #print(data)
    lowest_index = 0
    highest_index = 0
    new_list = []
    for x in range(len(data)):
        if data[x][1] >= 5.0:
            lowest_index = x
            #break used to prevent the loop from continuously running.
            break
    for x in range(len(data)):
        if data[x][1] >= 10.0:
            highest_index = x
            break

    for x in range(lowest_index, highest_index):
        new_list.append(data[x])

    for x in range(len(new_list)):
        print("The ID's of the items whose prices are between $5 and $10 are:",new_list[x][0])
(between5_10(readHtml()))
