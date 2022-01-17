"""
Recursion
By Joshua Blake-Williams
"""

# Function used to replace certain characters in a word.
# Input: string, one character to change, character to change to.
# Output: String with the characters swapped.
def replaceSep(myString, sep1, sep2):
    if len(myString) > 0: # Checks to see if the string has characters
        first = myString[0]
        if first == sep1:
            return sep2 + replaceSep(myString[1:], sep1, sep2) # Swaps first with sep2 if first is equal to sep1
        else:
            return first + replaceSep(myString[1:], sep1, sep2)# if the first char is not sep1 the function is recalled with the next char whilst storing the previous char
    else:
        return "" # if the string is empty then return nothing.

# Function used to count the number of siblings
# Input: a number (n)
# Output: the number of siblings people have.
def countSiblings(num_of_elves):
    if num_of_elves <= 0: # Checks to see if the number of elves is greater than zero
        return 0
    if num_of_elves %.2 == 0:
        return 1 + countSiblings(num_of_elves - 1) # If the number of elves is even then add one and call the function with n-1
    if num_of_elves % 2 != 0:
        return 3 + countSiblings(num_of_elves - 1) # if the number of elves is odd then add 3 and call rhe function with n-1

# Function created to determine whether or not a word is palindrome or not.
# Input: A string is taken in as the input
# Output: True or False depending on whether the word is palindrome or not.
def palindrome(string):
    if len(string) == 0: # If the length of the string is 0 it is palindrome
        return True
    if len(string) == 1: # If the length of the string is 1 it is also palindrome so we make these checks before checking the word.
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1]) # Gives the rest of the word to the function to test again
    if string[0] != string[-1]:
        return False

# Function used to extract a specific part of the string.
# Input: A String
# Output: string inclusive of its brackets.
def extractor(string):
    if len(string) == 0:
        return ""
    first = string[0] # first is set to the first character so it can be used to check for parenthesis.
    end = string[-1] # end is used for the same reason as above but just checking the final character instead.

    if first == "(" and end == ")": # if the string starts and ends with parentheses then return the whole string.
        return string
    elif first != "(":
       return extractor(string[1:]) # if the first char is not a parenthesis then the next character is passed on.
    elif end != ")":
        return extractor(string[:-1]) # if the last char is not a parenthesis then the next char  is passed on.

# Function created in order to execute each function to test their ability to complete the given tasks.
# Input: No parameter are used here
# Output: All the expected outcomes from each function
def Tester():
    print(replaceSep("hope*you*are*enjoying*the*course", "*", " "))
    print(replaceSep("Hi.  I am having fun.  Are you?", ".", "!!"))
    print(replaceSep("popopopopo", "p", "x"))
    print(replaceSep("xxxxx", "o", "b"))
    print(countSiblings(0))
    print(countSiblings(100))
    print(countSiblings(2))
    print(countSiblings(5))
    print(countSiblings(-9))
    print(extractor("(hello world)"))
    print(extractor("My country (of origin) is Canada"))
    print(extractor("I do not have any parenthesis"))
    print(palindrome("racecar"))
    print(palindrome("hello"))
    print(palindrome("redrumsirismurder"))
Tester()
