# Joshua Blake-Williams

import random
import time

# Generates a list of n integers, ranging from 1-n
def generateList(n):

	lst = []
	for i in range(n):
		lst.append(random.randrange(1, n+1, 1))

	return lst


# Sort the list using the bubble sorting algorithm
def sort(aList):
	length = len(aList) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if aList[i] > aList[i+1]:
				sorted = False
				aList[i], aList[i+1] = aList[i+1], aList[i]

	return aList

# Function that performs binary search
def binSearch(lst, first, last, target):

	start = time.process_time()

	if first > last:
		return -1
	else:
		mid = int((first + last) / 2)
		if lst[mid] == target:
			return lst[mid]
		elif lst[mid] > target:
			return binSearch(lst, first, mid-1, target)
		else:
			return binSearch(lst, mid+1, last, target)

# Function that performs trinary search
def trinSearch(lst, first, last, target):

	if first > last:
		return -1
	else:
		oneThird = int(first + (last-first) / 3)
		twoThirds = int(first + 2* (last-first) / 3)
		if lst[oneThird] == target:
			return oneThird
		elif lst[oneThird] > target:
			return trinSearch(lst, first, oneThird-1, target)
		elif lst[twoThirds] == target:
			return twoThirds
		elif lst[twoThirds] > target:
			return trinSearch(lst, oneThird+1, twoThirds-1, target)
		else:
			return trinSearch(lst, twoThirds+1, last, target)

# Used in experiment 2, creates a list of even integers
def evenArray(n):
	evens = []
	for x in range(n+1):
		if (x % 2) == 0:
			evens.append(x)
	return evens

# Also used in experiment 2, creates the search list of odd integers 
def oddArray(n):
	odds = []
	for x in range(n + 1):
		if (x % 2) == 1:
			odds.append(x)
	
	return odds	

# Everything was run in the main function to maintain test result order
def main():
	
	# --- Experiment 1 --- #

	# -- Binary Search -- #

	overall = time.process_time()

	# Generate list of size n = 1000
	print("For n = 1000: ")
	randomList = generateList(1000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	# Binary search for every value in the search list
	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)

	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 1000: ", str(elapsed), "\n")


	# Generate list of size n = 2000
	print("For n = 2000: ")
	randomList = generateList(2000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 2000: ", str(elapsed), "\n")


	# Generate list of size n = 4000
	print("For n = 4000: ")
	randomList = generateList(4000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)

	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 4000: ", str(elapsed), "\n")

	# Generate list of size n = 8000
	print("For n = 8000: ")
	randomList = generateList(8000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 8000: ", str(elapsed), "\n")


	# Generate list of size n = 16000
	print("For n = 16000: ")
	randomList = generateList(16000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 16,000: ", str(elapsed), "\n")

	totalElapsed = (time.process_time() - overall)
	print("Total time taken for Binary Search in Experiment 1: ", str(totalElapsed), "\n\n")


	# -- Trinary Search -- #

	overall = time.process_time()

	# Generate list of size n = 1000
	print("For n = 1000: ")
	randomList = generateList(1000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	# Binary search for every value in the search list
	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)

	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 1000: ", str(elapsed), "\n")


	# Generate list of size n = 2000
	print("For n = 2000: ")
	randomList = generateList(2000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 2000: ", str(elapsed), "\n")


	# Generate list of size n = 4000
	print("For n = 4000: ")
	randomList = generateList(4000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)

	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 4000: ", str(elapsed), "\n")

	# Generate list of size n = 8000
	print("For n = 8000: ")
	randomList = generateList(8000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 8000: ", str(elapsed), "\n")


	# Generate list of size n = 16000
	print("For n = 16000: ")
	randomList = generateList(16000)
	sortedList = sort(randomList)

	# Generate search list of size 10*n
	searchList = randomList * 10
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 16,000: ", str(elapsed), "\n")

	totalElapsed = (time.process_time() - overall)
	print("Total time taken for Trinary Search in Experiment 1: ", str(totalElapsed), "\n\n")

	# --- Experiment 2 --- #

	# -- Binary Search -- #
	overall = time.process_time()

	# Generate list of size n = 1000
	print("For n = 1000: ")
	evenList = evenArray(1000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(1000)) 
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)
	
	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 1000: ", str(elapsed), "\n")


	# Generate list of size n = 2000
	print("For n = 2000: ")
	evenList = evenArray(2000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(2000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 2000: ", str(elapsed), "\n")


	# Generate list of size n = 4000
	print("For n = 4000: ")
	evenList = evenArray(4000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(4000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 4000: ", str(elapsed), "\n")


	# Generate list of size n = 8000
	print("For n = 8000: ")
	evenList = evenArray(8000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(8000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 8000: ", str(elapsed), "\n")


	# Generate list of size n = 16000
	print("For n = 16000: ")
	evenList = evenArray(16000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(16000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		binSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Binary Search where n = 16000: ", str(elapsed), "\n")

	totalElapsed = (time.process_time() - overall)
	print("Total time taken for Binary Search in Experiment 2: ", str(totalElapsed), "\n\n")

	# -- Trinary Search -- #
	overall = time.process_time()

	# Generate list of size n = 1000
	print("For n = 1000: ")
	evenList = evenArray(1000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(1000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 1000: ", str(elapsed), "\n")


	# Generate list of size n = 2000
	print("For n = 2000: ")
	evenList = evenArray(2000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(2000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 2000: ", str(elapsed), "\n")


	# Generate list of size n = 4000
	print("For n = 4000: ")
	evenList = evenArray(4000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(4000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 4000: ", str(elapsed), "\n")


	# Generate list of size n = 8000
	print("For n = 8000: ")
	evenList = evenArray(8000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(8000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 8000: ", str(elapsed), "\n")


	# Generate list of size n = 16000
	print("For n = 16000: ")
	evenList = evenArray(16000)
	sortedList = sort(evenList) # Should already be sorted, but you never know

	# Generate search list of size 10*n
	searchList = (oddArray(16000))
	searchList = searchList * 10
	random.shuffle(searchList)
	searchList = set(searchList)

	start = time.process_time()
	for i in searchList:
		trinSearch(sortedList, 0, len(sortedList)-1, i)
	
	elapsed = (time.process_time() - start)
	print("Time taken for Trinary Search where n = 16000: ", str(elapsed), "\n")

	totalElapsed = (time.process_time() - overall)
	print("Total time taken for Trinary Search in Experiment 2: ", str(totalElapsed), "\n\n")

main()





















