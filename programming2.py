def meanBoutsPerPatient ():
	filename = "InflammatoryIBS.csv"
	inFile = open(filename, 'r')
	lines = inFile.readlines() #list of lines + \n
	for patientId, lineX in enumerate(lines, 1): #for item/line in list/lines: #iterate through each line
		lineX = lineX.strip() #	.strip() - remove \n from item/line
		lineX = lineX.split(',') #	.split(',') - split the string list at each comma - comma is an element of the list
		list1, list2 = [], []  #create empty list - at each iteration in lines - append non-comma strings to the list #emptylist - each iteration in lines - append int(elements of list1) #list1,list2 = [],[]
		for index, value in enumerate(lineX): #for loop to append values onto list1
			if lineX[index] == ',': 
				index += 1
			else:
				list1.append(value) #append non-comma strings/values to the list
		#print(list1[2]) - print statement show that the comma is not an element of list1
		list2 = [int(element) for element in list1] #listcomprehension = [expression iterator conditional]
		#print(list2) #- shows they're integers
		sumOfBouts = 0 #accumulator, initialised to zero
		for boutNumber in list2: #sum - for loop - add up the integer elements in that line(iteration)
			sumOfBouts += boutNumber #sum = sum + boutNum
		averageBouts = sumOfBouts / len(list2) #average - sumOfBouts/ len(list2)
		#print(sumOfBouts)
		#print(averageBouts) #need to round to whole number
		averageBouts = round(averageBouts)
		#print(averageBouts)
		print ("Patient", patientId, "had", averageBouts, "inflammatory bouts on average")

	inFile.close()



def meanBoutsAcrossAllPatients ():
	filename = "InflammatoryIBS.csv"
	inFile = open(filename, 'r')
	lines2 = inFile.readlines()
	listB = [] #one big long list of integers
	for lineY in lines2: #for item in list of lines
		lineY = lineY.strip() #removes \n by default
		lineY = lineY.split(',') #splits at comma - gives me a list
		listA = [] #list with all non comma strings
		for index, value in enumerate(lineY): #for loop to append values onto listA
				if lineY[index] == ',': 
					index += 1
				else:
					listA.append(value)
		#print(listA[2]) - print statement show that the comma is not an element of listA
		for element in listA: # for element in list
			listB.append(int(element)) #append int(element in list1) to listB

	sumBouts2 = 0 
	for bout in listB:
		sumBouts2 += bout

	#average = sumBouts2 / len(listB)
	avgBoutsPatients = sumBouts2 / len(listB)
	

	
	print ("The average number of inflammatory bouts on this trial medication is: ", avgBoutsPatients)

	inFile.close()
		
meanBoutsPerPatient() #invoking first function
meanBoutsAcrossAllPatients() #invoking second function


def meanBoutsPerPatient ():    
	filename = "InflammatoryIBS.csv"    
	inFile = open(filename, 'r')    
	meanPerPatient = []    
	lines = inFile.readlines() #list of lines + \n
	for patientId, lineX in enumerate(lines, 1): #for item/line in list/lines: #iterate through each line
		lineX = lineX.strip() #	.strip() - remove \n from item/line
		lineX = lineX.split(',') #	.split(',') - split the string list at each comma - comma is an element of the list
		list1, list2 = [], []  #create empty list - at each iteration in lines - append non-comma strings to the list #emptylist - each iteration in lines - append int(elements of list1) #list1,list2 = [],[]
		for index, value in enumerate(lineX): #for loop to append values onto list1
			if lineX[index] == ',': 
				index += 1
			else:
				list1.append(value) #append non-comma strings/values to the list
			#print(list1[2]) - print statement show that the comma is not an element of list1
		list2 = [int(element) for element in list1] #listcomprehension = [expression iterator conditional]
		#print(list2) #- shows they're integers
		sumOfBouts = 0 #accumulator, initialised to zero
		for boutNumber in list2: #sum - for loop - add up the integer elements in that line(iteration)
			sumOfBouts += boutNumber #sum = sum + boutNum
		averageBouts = sumOfBouts / len(list2) #average - sumOfBouts/ len(list2)
		#print(sumOfBouts)
		meanPerPatient.append([patientId, averageBouts])
		#print(averageBouts)
 
	inFile.close()    
	return meanPerPatient




