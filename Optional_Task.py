# Compulsory Task 2

# This opens the numbers1 text file and writes the line into a string
numbers1 = open ('numbers1.txt','r+')
getNumbers1 = ''
for line in numbers1:
    getNumbers1 = getNumbers1 + line
numbers1.close()
    
# The string of numbers then gets split into a list
getNumbers1 = getNumbers1.split()

# This opens the numbers2 text file and writes the line into a string
numbers2 = open ('numbers2.txt','r+')
getNumbers2 = ''
for line in numbers2:
    getNumbers2 = getNumbers2 + line
numbers2.close()

# The string of numbers then gets split into a list
getNumbers2 = getNumbers2.split()

# Declaring a new list which will contain all the numbers and setting it eaul to the first list of numbers
allNumbers = getNumbers1

# Adding every number in the second list of numbers to the list of first numbers so that they are all in one list
for number in getNumbers2:
    allNumbers.append(number)

# The numbers are in string form so a new empty list is created to cast them and put them in a new list   
allNumbersInt = []
for number in allNumbers:
    allNumbersInt.append(int(number))

# The numbers then get sorted into ascending order
allNumbersInt.sort()

# The sorted list then needs to be cast back to a string
allNumbersStr = []
for number in allNumbersInt:
    allNumbersStr.append(str(number))

# This takes the numbers out of the list and back into a string to be able to write it to the text file
stringNum = ''
for i in range (0,len(allNumbersStr)):
    stringNum = stringNum + allNumbersStr[i]  + " "

print (stringNum)

# This opens the allNumbers file and saves the string in it as a line
allNumbers = open ('allNumbers.txt','w')
allNumbers.write(stringNum)
allNumbers.close()
