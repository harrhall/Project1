import os
import filecmp
from dateutil.relativedelta import *
from datetime import date, timedelta

def getData(file):
	inFile = open(file, "r")
	line = inFile.readline()
	dictList = []
	while line:
		thisDict = {}
		values = line.split(",")
		first = values[0]
		last = values[1]
		email = values[2]
		year = values[3]
		dob = values[4]
		thisDict["First"] = first
		thisDict["Last"] = last
		thisDict["Email"] = email
		thisDict["Class"] = year
		thisDict["DOB"] = dob
		dictList.append(thisDict)
		line = inFile.readline()
	inFile.close()
	del dictList[0] # Deletes the first element, which was just the column headers
	return dictList

# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows


def mySort(data,col):
	sortedList = sorted(data, key=lambda k: k[col])
	x = sortedList[0]
	return (x["First"] + " " + x["Last"])

def classSizes(data):
	num_sr = 0
	num_jr = 0
	num_so = 0
	num_fr = 0
	for i in data:
		if i['Class'] == 'Senior':
			num_sr += 1
		elif i['Class'] == 'Junior':
			num_jr += 1
		elif i['Class'] == 'Sophomore':
			num_so += 1
		elif i['Class'] == 'Freshman':
			num_fr += 1
	l = [("Senior",num_sr), ("Junior",num_jr), ("Sophomore",num_so), ("Freshman",num_fr)]
	return sorted(l, key=lambda k: k[1], reverse = True)

# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]


def findMonth(a):
	num_1 = 0
	num_2 = 0
	num_3 = 0
	num_4 = 0
	num_5 = 0
	num_6 = 0
	num_7 = 0
	num_8 = 0
	num_9 = 0
	num_10 = 0
	num_11 = 0
	num_12 = 0
	for i in a:
		val = i['DOB'].split('/')[0] #splits the key for DOB of each dictionary at the slash
		if val == '1':
			num_1 += 1
		elif val == '2':
			num_2 += 1
		elif val == '3':
			num_3 += 1
		elif val == '4':
			num_4 += 1
		elif val == '5':
			num_5 += 1
		elif val == '6':
			num_6 += 1
		elif val == '7':
			num_7 += 1
		elif val == '8':
			num_8 += 1
		elif val == '9':
			num_9 += 1
		elif val == '10':
			num_10 += 1
		elif val == '11':
			num_11 += 1
		elif val == '12':
			num_12 += 1
	new_l = [(1,num_1),(2,num_2),(3,num_3),(4,num_4),(5,num_5),(6,num_6),(7,num_7),(8,num_8),(9,num_9),(10,num_10),(11,num_11),(12,num_12)]
	new_l_2 = (sorted(new_l, key=lambda k: k[1], reverse = True)[0]) #sort the list by values
	return new_l_2[0] #return the month for the highest value tuple ^QUESTION Why does the testcase still check if it returns 3, when the data still has 2 3 and 9 at the same frequency
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

def mySortPrint(a,col,fileName):
	x = open(fileName, 'w')
	sortedList = sorted(a, key=lambda k: k[col])
	for i in sortedList:
		x.write(str(i["First"]) + "," + str(i["Last"]) + "," + str(i["Email"]) + "\n")
	x.close()

def findAge(a):
	birthList = []
	newList = []
	ageList = []
	finalList = []
	counter = 0
	for i in a: #loop through input, add DOBs to birthList
		birthList.append(i["DOB"][:-1]) #add DOB to birthList but dont include the newline character
	for x in birthList: #loop through birthList, split at '/'
		newList.append(x.split("/")) #add the split births to newList
	for y in newList:
		ageList.append(date.today() - date(int(y[2]), int(y[0]), int(y[1]))) #subtracts birth date from today's date
	for z in ageList:
		finalList.append(z / timedelta(days = 365.2422)) #^QUESTION: Test says the output should be 40 but its 41, is this because I'm assuming today's date and the test case isnt?
	for a in finalList:
		counter += a #adds the ages (in floats of years) together
	counter = counter / len(finalList) #divides that number by the number of elements (people)
	return round(counter) #returns that average rounded to the nearest int


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
