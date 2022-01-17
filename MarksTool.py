"""-------
Joshua Blake-Williams
Marks Tool
--------"""

import urllib.request #Allows the library needed to be used.
import time
#Input: wedsite Output: Data
def readWordList():
    #reads in the data from the website.
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/marks.txt")
    html = response.readline()
    data = []
    #Makes sure each line is read in.
    while len(html) != 0:
        line = html.decode('utf-8').split()
        data.append(line)
        html = response.readline()

# Changes the marks in the list into a float so calculations can be carried out.
        for x in range(1,len(data)):
            for i in range (1,7):
                data[x][-1] = float(data[x][-1])
                if i > 0:
                    data[x][i] = float(data[x][i])
    data.pop(0)
    return data
#Input: data
#Output: Final marks for each student
def finalMarkCalculator(data):
# for loop is used here to traverse through each sub-list(student)
    for student in range (len(data)):
        finalMark = 0.0
        a_weight = 0.0
        # Loop to go through each mark in studnet
        for mark in range (len(data[student])):
            if mark == 1:
                finalMark += (data[student][mark]/24) * 5
            if mark == 2:
                finalMark += (data[student][mark]/23) * 5
            if mark == 3:
                finalMark += (data[student][mark]/13) * 5
            if mark == 4:
                finalMark += (data[student][mark]/18) * 5
            if mark == 5:
                finalMark += (data[student][mark]/18) * 5
            # Here I inserted midterm marks and final marks so that I could eliminate the need for more functions.
            if mark == 6:
                finalMark += (data[student][mark]/35) * 30
            if mark == 7:
                finalMark += (data[student][mark]/65) * 45
        #once all the marks have been added up they are added to the end of each og those students
        data[student].append(round(finalMark,2))
    return data
# the data functions hold the data list that i need to use in the next function
#was used for ease of transmission
def dataHolder():
    data = finalMarkCalculator(readWordList())
    return data
#Function calculates the Letter Grade based on the final mark that they have.
#Input: takes data with list of lists
#Output: each student has a letter grade added to their record
def LetterGrade(data):
    #data = dataHolder()
    # used to traverse through each students records
    for student in range (len(data)):
        #this assigns the final mark to the last element in the students records
        finalMark = data[student][-1]
        a = round(finalMark)
        #Letters are appended to the end of the students lists and stored there
        if finalMark >= 90 and finalMark <= 100:
            data[student].append("A+")
        if finalMark >= 85 and finalMark <= 89:
            data[student].append("A")

        if finalMark >= 80 and finalMark <= 84:
            data[student].append("A-")

        if finalMark >= 77 and finalMark <= 79:
            data[student].append("B+")

        if finalMark >= 73 and finalMark <= 76:
            data[student].append("B")

        if finalMark >= 70 and finalMark <= 72:
            data[student].append("B-")

        if finalMark >= 67 and finalMark <= 69:
            data[student].append("C+")

        if finalMark >= 63 and finalMark <= 66:
            data[student].append("C")

        if finalMark >= 60 and finalMark <= 62:
            data[student].append("C-")

        if finalMark >= 57 and finalMark <= 59:
            data[student].append("D+")

        if finalMark >= 53 and finalMark <= 56:
            data[student].append("D")

        if finalMark >= 50 and finalMark <= 52:
            data[student].append("D-")

        if finalMark <= 49.0:
            data[student].append("F")

    return data
#Data function as explained above
def dataHolder2():
    data = LetterGrade(dataHolder())
    return data
#Function which converts the grade of each student into a number based on the letter
#Input:data from previous function
#Output:New data which contains the number grade now also.
def Letter2GradeConv(data):
    #data = dataHolder2()
    #Used to traverse through the students records then add their number gpa to the end of their record
    for student in range (len(data)):
        letterGrade = data[student][-1]
        if letterGrade == "A+":
            data[student].append(4.30)

        if letterGrade == "A":
            data[student].append(4.00)

        if letterGrade == "A-":
            data[student].append(3.70)

        if letterGrade == "B+":
            data[student].append(3.30)

        if letterGrade == "B":
            data[student].append(3.00)

        if letterGrade == "B-":
            data[student].append(2.70)

        if letterGrade == "C+":
            data[student].append(2.30)

        if letterGrade == "C":
            data[student].append(2.00)

        if letterGrade == "C-":
            data[student].append(1.70)

        if letterGrade == "D+":
            data[student].append(1.30)

        if letterGrade == "D":
            data[student].append(1.00)

        if letterGrade == "D-":
            data[student].append(0.70)

        if letterGrade == "F":
            data[student].append(0.00)
    return data
#Same as above
def dataHolder3():
    data = Letter2GradeConv(dataHolder2())
    #print(data)
    return data
#Function created for the first choice in the menu
#Input: Data list from above
#Output: Display of specific students marks
def displayMarks():
    #data is read in
    data = dataHolder3()
    #allows the user to choose which students records they wish to see
    student_number = input("Please enter a student number(from 2000 to 2104): ")
    for student in data:
        for number in student:
            #checks to see if the student number is equal to the number in the students records
            if student_number == number:
                return student
#Function created for choice number 2
#Input: Takes the big data list from previous and searches through
#Output:Releases all the students who have marks below 50
def below50(data):
    new_data = []
    # goes through each students records
    for student in data:
        #if the final mare was below 50% of the mark then store the following positions in a list and store it
        if student[-4] < 32.5:
            new_data.append(student[0])
            new_data.append(student[7])
            new_data.append(student[-1])
        return new_data
#same as above
def dataHolder4():
    data = below50(dataHolder3())
    return data
#Function created for choice number 3
#Input: Takes the big data list in
#output: releases all the student who have marks in the midterm and fina that are over 80%
def above80():
    data = dataHolder3()
    #print(data)
    new_data = []
    #Goes through each students records
    for student in (data):
        # checks to see if the mid term marks for each student and the final marks are above 80% then outputs them
        if student[-4] > 52.0 and student[-5] > 28:
            #print(student)
            new_data.append(student[0])
            new_data.append(student[-5])
            new_data.append(student[-4])

            return new_data
#Funuction for choice number 4
#Input: Takes the data list in with students information
#Output: Releases all/the the student(s) with the highest mark(s)
def highestMark():
    data = dataHolder3()
    highest_mark_list = []
    #Traverses through each students records
    for student in range (len(data)):
        #stores the 7th element of the students records in another list
        highest_mark_list.append(data[student][7])
        #Sorts the list with the final marks into descending order
        highest_mark_list.sort(reverse=True)

    dummy = False
    while dummy != True:
        # Goes through the records of each student
        for student in range (len(data)):
            #checks to see if the first element in the new list is equal to the final mark in each students records
            if highest_mark_list[0] == data[student][7]:
                #Outputs the users student number final mark and gpa if they have the highest exam mark.
                print("Student:",data[student][0], "Final:",data[student][7], "GPA:",data[student][8])

            dummy = True
#Function created for choice number 5
#Input: The data is passed in
#Output: Each students mark is boosted by 5% unless its already 100%
def exam_incr():
    data = dataHolder3()
    new_data = []
    #Traverses through the students records
    for student in range(len(data)):
        final_mark = 0.0
        for mark in range(len(data[student])):
            if mark == 7:
                final_mark += (((data[student][mark] * 1.05)))
                if final_mark > 65:
                    final_mark == 65
                data = readWordList()
                data[student][7] = final_mark

                finalMarkCalculator(data)
                LetterGrade(data)
                Letter2GradeConv(data)
                return data
#function for choice number 6
#Input:Takes the data of the students in
#Output: Average of the assignments of each student and stores and shows it
def averageAss():
    data = dataHolder3()
    for student in range (len(data)):
        finalMark = 0.0
        average = 0.0
        for mark in range (len(data[student])):
            if mark == 1:
                finalMark += (data[student][mark]/24)
            if mark == 2:
                finalMark += (data[student][mark]/23)
            if mark == 3:
                finalMark += (data[student][mark]/13)
            if mark == 4:
                finalMark += (data[student][mark]/18)
            if mark == 5:
                finalMark += (data[student][mark]/18)

        average += (finalMark / 5) * 100

        return round(average, 2)
#Function for choice number 6
#Input: Data is input
#Output: Midterm average
def averageMid():
    data = dataHolder3()
    for student in range (len(data)):
        mid_mark = 0.0
        average = 0.0
        for mark in range (len(data[student])):
            if mark == 6:
                mid_mark += (data[student][mark]/35)
        average += mid_mark * 100

        return round(average, 2)
#Function for choice number 6
#Input: Data which contains the information on students
#Output: Final average
def averageFin():
    data = dataHolder3()
    for student in range (len(data)):
        fin_mark =0.0
        average = 0.0
        for mark in range (len(data[student])):
            if mark == 7:
                fin_mark += (data[student][mark]/65)
        average += fin_mark * 100

        return round(average, 2)
#Function which is used to start off all of the program and provide a user interface for someone to interact with.
#Input: The preceding functions are passed in in a specific order
#Output: A user interface and a desired result for the user
def main():
    dummy = False
    print("Hello, you may now choose from the choices listed below")
    time.sleep(2)
    print("1. Enter a student number to see all their marks.")
    print("2. Display the(student no, gpa, final) for those who scored the highest on the exam.")
    print("3. Display the (student no, gpa, final) for those who score below 50 on the exam.")
    print("4. Display the students (student no, midterm, final) of those who scored > 80 on the exam.")
    print("5. increase all the final exam grades by 5%. (then view)")
    print("6. calculate the average you want")
    print("7. Quit. :(")
    time.sleep(2)
    #takes user input
    user_choice = int(input("Enter your choice: "))
    #Each choice is output here
    while dummy != True:
        if user_choice == 1:
            print(displayMarks())
        elif user_choice == 2:
            highestMark()
        elif user_choice == 3:
            print("['Student no',GPA, Final]")
            print(below50(dataHolder3()))
        elif user_choice == 4:
            print("['student no', Midterm, Final]")
            print(above80())
        elif user_choice == 5:
            print("This is the list with final exams boosted by 5% position [-3]")
            print(exam_incr())
        elif user_choice == 6:
            user_choice_2 = int(input("1. Average of 5 assignments\n2. Average on midterm\n3. Average on final\n"))
            if user_choice_2 == 1:
                print(averageAss())
            elif user_choice_2 == 2:
                print(averageMid())
            elif user_choice_2 == 3:
                print(averageFin())
        elif user_choice == 7:
            quit()
        elif user_choice != 1 or 2 or 3 or 4 or 5 or 6 or 7:
            print("incorrect entry")
            user_choice = int(input("Enter your choice: "))
        dummy = True
main()
