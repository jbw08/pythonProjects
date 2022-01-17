"""
Chore list (Linked Lists)
By Joshua Blake-Williams
"""

import urllib.request
import time

# Initial read in of the websites contents producing a list to create a linked list
def readHtml():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/todo.txt")
    html = response.readline()
    data = []
    #at this point you have a list representing this item -- create a linked list node for this item
    #an add it to the existing list.
    while len(html) != 0:
        line = html.decode('utf-8').split()
        data.append(line)
        html = response.readline()


    #swap = True
    #end = len(data) - 1
    #while swap:
     #   swap = False
      #  for i in range (end):
       #     if data[i][4] > data[i+1][4]:
        #        #if there has been a swap, then swap is set to true, otherwise it is not.
         #       data[i], data[i+1] = data[i+1], data[i]
          #      swap = True
        #end -= 1
    return data

## function which allows the top pointer to point to a new item
def addToHead(aList,value):
    #create a new node to add
    newNode = {} # Empty dictionary
    newNode["data"] = value
    newNode["next"] = aList
    return newNode
# function to identify exactly where a specific element is
def nodeContainingX(linkedList,value):
    ptr = linkedList
    while ptr != None and ptr["data"] != value:
        ptr = ptr["Next"]
    #Ptr will either be None (Didn't find the value) or will be the desired node.
    return ptr
# Function which allows elements to be inserted into the list in specific places
def addToMiddle(aList,value,newValue):
    node = {}
    node["data"] = newValue
    # call node containingX to get the node containing "value" (or none if it doesn't exist)
    before = nodeContainingX(aList, value)
    if before == None:  # value doesn't exist
        return aList  # just return the head of the unchanged list
    # attach the new node to the node that "before" points to currently
    node['next'] = before['next']
    # link before to the new node
    before['next'] = node
    return aList  # the head of the list doesn't change - return it
# function which actually creates the linked list
def createList(aList):
    linkedList = None #creates a new empty list
    for i in aList:
        linkedList = addToHead(linkedList, i)
    return linkedList # return the head of the new list.
# fucntion which prints the linked list with arrows
def printList(aList):
    ptr = aList
    while ptr != None:
        print(ptr["data"], "->", end= " ")
        ptr = ptr["next"]
    print("None")

# reads in the commands from the website provided allowing us to see what needs to be done
def commandsFile():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/driver.txt")
    html = response.readline()
    didIt = []
    while len(html) != 0:
        line = html.decode('utf-8').split()
        didIt.append(line)
        html = response.readline()
    return didIt

# This function allows the to do linked list to be created.
# taking no parameters and calling another function produces the list you will see.
def printToDo():
    print("The To-do list is now being gathered...")
    time.sleep(2)
    print("Here is the list of all the tasks that need to be completed:")
    aList = createList(readHtml())
    printList(aList)

# This function will allow the did it list to be output to see what tasks have been completed.
# taking no parameters and calling other functions in order to complete this task.
def printDidIt():
    print("The Did-It list is now being gathered...")
    time.sleep(2)
    print("Here is the did it list")
    didIt = createList(commandsFile())
    printList(didIt)

# This function will allow the new tasks to be added to the to-do list
# Taking the commands in as a list to add the right element to the current to do list
def addToDo():
    toAdd = []
    user_choice = input("Enter the task you wish to add to the list, in the following order: Task name, time required to complete class(mins), date that it needs to be completed by.\n")
    toAdd.append(user_choice.split())
    addToHead(createList(readHtml()),toAdd)
    print("adding your task to the list.")
    time.sleep(2)
    print("Your task has now been added to the To-Do list.")

# This function is used to calculate the length of the linked list
# Taking a list in as its' parameter
def getLength(aList):
    # returns the length (number of elements) of the linked list aList
    count = 0
    ptr = aList
    while ptr != None: # iterate through the list
        count += 1
        ptr = ptr["next"] # move pointer to next element in the list
    return count

# This function will be used to get  a specific element to the list
# taking the linked list in as a parameter as well as the index number of the element you wish to select.
def getElement(linkedList, index):
    spotChecked = linkedList # initialises the pointer variable
    if index > getLength(linkedList): # Checks that the index that we are checking for isn't bigger than the actual list
        return None # if no value found --> return None
    for i in range(0, index): # goes through the list up until index
        spotChecked = spotChecked["next"]
    return spotChecked["data"] #returns the value found

# Function was created in order to execute the tasks that are in the To-Do list.
# Takes the linked list in as a parameter in order to manipulate it.
def executeTask(aList):
    didIt = []
    aList = createList(readHtml())
    print("Here is the current To-Do list:", end = "")
    printList(aList)
    user_choice = int(input("Enter a number from 1-8 (inclusive) to execute a task from the to-Do list: "))
    if user_choice ==1:
        didIt.append(getElement(aList, 1))
        print("Task 1 is being executed....")
        time.sleep(2)
        print("Task 1 is now complete")
    if user_choice == 2:
        didIt.append(getElement(aList, 2))
        print("Task 2 is being executed...")
        time.sleep(2)
        print("Task 2 is now complete")
    if user_choice == 3:
        didIt.append(getElement(aList, 3))
        print("Task 3 is being executed...")
        time.sleep(2)
        print("Task 3 is now complete")
    if user_choice == 4:
        didIt.append(getElement(aList, 4))
        print("Task 4 is being executed...")
        time.sleep(2)
        print("Task 4 is now complete")
    if user_choice == 5:
        didIt.append(getElement(aList, 5))
        print("Task 5 is being executed...")
        time.sleep(2)
        print("Task 5 is now complete")
    if user_choice == 6:
        didIt.append(getElement(aList, 6))
        print("Task 6 is being executed...")
        time.sleep(2)
        print("Task 6 is now complete")
    if user_choice == 7:
        didIt.append(getElement(aList, 7))
        print("Task 7 is being executed...")
        time.sleep(2)
        print("Task 7 is now complete")
    if user_choice == 8:
        didIt.append(getElement(aList, 8))
        print("Task 8 is being executed...")
        time.sleep(2)
        print("Task 8 is now complete")
    if user_choice != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
        print("Sorry, the task you have chosen is unavailable.")
    # creation of the dit it linked list as each new task is added to it.
    didItLinked = createList(didIt)
    # variable used to show the linked list as tasks are being executed.
    outputDitIt = printList(didItLinked)
    return outputDitIt

# main function has been created in order to allow the execution of the program
def main():
    didIt = []
    print("Welcome to the chore list program.")
    print ("Please select a menu option:")
    print("To view the tasks that need to be done press 1.")
    print("To view the Did it list press 2.")
    print("To execute any of the tasks on the to do list press 3.")
    print("To add a task press 4.")
    print ("5) Exit the program.")
    user_input = int(input("Enter your choice now: "))
    while True:
        if user_input == 1:
            printList(createList(readHtml()))
        elif user_input == 2:
            print(didIt)
        elif user_input == 3:
            aList = createList(readHtml())
            executeTask(aList)
        elif user_input == 4:
            addToDo()
        elif user_input == 5:
            print ("Thank you for using the program!")
            break
        else:
            print ("You did not enter a valid menu option.")

main()
