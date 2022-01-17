# Joshua Blake-Williams


# Used to keep track of how many times i reached 10 and was not able to insert
# the given value. This var is used to determine the table size.
overTen = 0
doubleHashNum = 0
# I didn't understand the wording of this assignment at first (or second) so
# I had to create this global variable 'doubleHashNum' to keep track of whether
# it's the first, second, or third test of double hashing


# Hashing function h'(k) that converts a string to a complex number.
# The method used is similar to Dan Berstein's version of the multiplication method,
# however customized from the value of 'a' in h(k) to the quadratic probing algorithm
# implimented. 
def hash0(k):
    a = 4909
    for x in k:
        a = a*7 * ord(x)
    return a

# Hashing function h''(k) that returns the sum of each letter of the code word
# (param provided) squared, and makes sure that it is an odd number.

def hash1(k):
    t = 0
    for z in k:
        t += ord(z)^2
    if t % 2 == 1:
        return t
    else:
        return t+1

# Another hashing function used for the double Hashing portion of this assignment
def hash2(k):
    x = (((k/2) * 27) % 27399)
    x = int(x)
    if x % 2 == 1:
        return x
    else:
        return x + 1

# Quadratic Probing Function:
# This function gets its hash value from h(k) and performs quadratic probing.
def qProbe(code, c1, c2, keys, size):
    global overTen
    i = 0
    v = hash0(code)
    a = v % size

    while (i < size) and (keys[a] != None):
        i += 1
        a = (v + c1*i + int(c2*i)^2) % size

        # If 10 inserts were tried
        if i > 10:
            overTen += 1
            break
        
    if keys[a] == None: # If empty, insert
        keys[a] = code

# Double Hashing Function:
# This function gets its hash value from h'(k) and h''(k) and performs the double hashing process.
def dHash(code, keys, size):
    global overTen, doubleHashNum
    i = 0
    a = hash0(code)
    b = hash1(code)
    
    if doubleHashNum == 1:
        a = hash2(a)
        b = hash0(code)
        b = hash2(b)
    elif doubleHashNum == 2:
        a = hash1(code)
        a = hash2(a)
        b = hash0(code)
        b = hash2(b)
      
    x = (a + b) % size

    while (i < size) and (keys[x] != None):
        i += 1
        x = (a + i*b) % size

        if i > 10:
            overTen += 1
            break

    if keys[x] == None:
        keys[x] = code
            
# Main function that opens the file and stores each code name in an array,
# preparing it for both quadratic probing and double hashing.
# For this assignment, I chose to submit this one class where both experiments
# are performed (as opposed to two separate classes). To make things simple,
# I used keys1 for Quadratic Probing and keys2 for Double Hashing.
# Similarily, I used words1 and words2 to differenciate the two experiments' attributes.
def main():
    # FOR TESTING
    global overTen, keys1, keys2, keys3, keys4, keys5, keys6, doubleHashNum
    words1 = []

    # Create an array with all the code names to choose from
    with open("file.txt", "r") as f:
        for line in f:
            words1.append(line.rstrip("\n"))
                          
    # Quadratic Probing #
    print("Quadratic Probing")
    print("Size 4639:")
    size = 4639
    keys1 = [None] * size
    for codeWord in words1:
        qProbe(codeWord, 1, 1, keys1, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0

    print("Size 4481:")
    size = 4481
    keys2 = [None] * size
    for codeWord in words1:
        qProbe(codeWord, 2, 0.5, keys2, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0

    print("Size 4261:")
    size = 4261
    keys3 = [None] * size
    for codeWord in words1:
        qProbe(codeWord, 3, 0.25, keys3, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0

    # Double Hashing #
    print("Double Hashing: ")
    print("Size 3769:")
    size = 3769
    keys4 = [None] * size
    for codeWord in words1:
        dHash(codeWord, keys4, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0
    doubleHashNum += 1

    print("Size 4229: ")
    size = 4229
    keys5 = [None] * size
    for codeWord in words1:
        dHash(codeWord, keys5, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0
    doubleHashNum += 1
    
    print("Size 3797: ")
    size = 3797
    keys6 = [None] * size
    for codeWord in words1:
        dHash(codeWord, keys6, size)
    print("Occurrences where i > 10: ", overTen)
    overTen = 0
    
# Run the damn thing
main()












