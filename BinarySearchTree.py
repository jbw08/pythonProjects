"""
Binary Search Tree
Created by: Joshua Blake-Williams
"""



# adds a value to a BST and returns a pointer to the modified BST
def add(tree, value):
    # if the tree is empty then return nothing
    if tree == None:
        return {'data': [value], 'left': None, 'right': None}
    elif value < tree['data'][0]:
        # if the value is less than the next value then it is added to the left other wise
        # it is added tp the right side
        tree['left'] = add(tree['left'], value)
        return tree
    elif value > tree['data'][0]:
        tree['right'] = add(tree['right'], value)
        return tree
    else:  # value == tree['data']
        return tree  # ignore duplicate
#Function which changes the each of the names to leif and stores it below their names
# Input: tree
# output: Names changed to Leif
def changeLeaves (tree):
    # if tree is empty then essentially do nothing
    if tree == None:
        return None
    # add LEIF in for each name
    elif tree["left"] == None and tree["right"] == None:
        tree["data"][0] = ("LEIF")
        return tree
    changeLeaves(tree["left"])
    changeLeaves(tree["right"])
    return tree
# Function created to count each of the nodes
# input: tree
# Ouput: The number of nodes in the BST
def countNodes(tree):
    if tree == None:
        return 0
    # findes all the nodes with names that begin with w
    # then adds up the number of nodes with w in it and returns that number
    if tree["data"][1][0] == "w" or tree["data"][1][0] == "W":
        return 1 + countNodes(tree["left"]) + countNodes(tree["right"])
    else:
        return countNodes(tree["left"]) + countNodes(tree["right"])
# Function created to change the order of the BST
# input: BST
#Output: reversed left and right sides
def printReverse(tree):
    # if the tree is empty then do nothing
    if tree == None:
        return None
    # otherwise output the left and right side swapped
    printReverse(tree["right"])
    printReverse(tree["left"])
# Funtion which print the values of the BST
# input: BST
# Output: The values of the tree sideways
def printValues(tree):
    # if the tree is empty then do nothing
    if tree == None:
        return None
    # prints the values of the tree
    printValues(tree["left"])
    printValues(tree["right"])
#function: used to see the BST
#Taken from sample code
def display(tree, indent=0):
    if tree == None: # empty
        pass
    else:
        # right tree first (so it's on the right when you tilt your
        # head to the left to look at the display)
        display(tree['right'],indent+1)
        print("    " * indent + str(tree['data']))
        # now the left tree
        display(tree['left'],indent+1)
#Main running function to show the execution of each of the functions
def main():
    # Dummy variable used to combine the functions in order to ensure they test properly
    # Taken from sample code
    tester = None
    tester = add(tester, [2, "Wayne"])
    tester = add(tester, [17, "Jane"])
    tester = add(tester, [1, "Wiggy"])
    tester = add(tester, [11, "Ziggy"])
    tester = add(tester, [20, "Ellen"])
    tester = add(tester, [19, "Wesley"])

    display(tester, 0)
    printValues(tester)
    changeLeaves(tester)
    display(tester, 0)
    printReverse(tester)
main()
