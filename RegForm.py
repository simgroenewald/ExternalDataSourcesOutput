# Compulsory Task 2

# This allows the user to enter the number of students registering
numStudents = input ("How many students will be registering: ")
numStudents = int(numStudents) # Casts the value to in integer
RegForm = open("RegForm.txt","w") # Creates the file that it will be stored in
allId = "" # Declares an empty string variable

# Runs for the number of students entered by the user and then allows that number of students to enter their ID numbers
for i in range (0,numStudents):
    idNum = input ("Please enter your ID number: ")
    idNumString = (idNum + "\n")
    allId = allId + idNumString # Saves them all in one string

RegForm.write(allId) # Writes the string to the text file
RegForm.close # Closes the text file
