import random
import string
import time



def getRooms():

	rooms = []
	capacity = []
	numRooms = int(0)
	while (int(numRooms) <= 0):
		numRooms = (input("How many rooms are there? "))
		if (numRooms == ''):
			numRooms = -1
	yesNo = 'q'
	while (yesNo.lower() != 'y' and yesNo.lower() != 'n'):
		yesNo = 'n' #################################3str(input("Would you like to name or number the rooms? "))

	###########EDIT
	


	if (yesNo[0].lower() == 'y'):

		for num in range(0,int(numRooms)):
			getName = input("What would you like to label room"+str(num+1)+"? ")
			if (getName == ''):
				rooms.insert(num, "Room "+str(num+1))	
			else:
				rooms.insert(num, getName)

	if (yesNo[0].lower() == 'n'):
		for num in range (0, int(numRooms)):
			rooms.insert(num, "Room "+str(num+1))

	#print (yesNo, numRooms)
	yesNo = 'q'
	while (yesNo.lower() != 'n' and yesNo.lower() != 'y'):
		yesNo = 'y' #######################################str(input("Do all the rooms seat the same number of people? "))
	
#############################EDIT

	

	defaultCap = 20 ###################################input("What is the default/average size of the rooms? ")
		
	if (yesNo[0].lower() == 'n'):

		for num in range(0,int(nusmRooms)):
			roomCap = 0
			#print("room"+str(num))
			roomCap = input("Capactity of "+str(rooms[num])+"? ")
			if (str(roomCap[:]) in string.ascii_letters) or (roomCap == ''):
				roomCap = defaultCap
			capacity.append(str(roomCap))

	
	return rooms, capacity
			
def setSchedule():

	yesNo = 'q'
	days = []
	hours = []
	start = []
	grid = []
	#breakdown = {}
	

	
	# temp = 0
	# for i in range (0, (24*4+1)):
	# 	breakdown2.append(temp)
	# 	temp += .25

	#print(breakdown2)

	numDays = 0
	while (numDays == 0):
		numDays = int(input("How many days long is this event? "))



	for num in range (0, int(numDays)):
		
		startTime = 0
		endTime = 24
		count = 0
		precount = 0
		breakdown2 = []
		breakdown = []
		grid.append([])


		temp = 0

		for i in range (0, (24*4+1)):
			breakdown2.append(temp)
			temp += .25

		days.append(1)
		getHours = input("How many hours on the day number "+str(num+1)+"? ")
		hours.append(float(getHours))
		getStart = input("What time does day number "+str(num+1)+" start (9am = 9, 4:45pm = 16.75) ? ")
		start.append(getStart)	

		#breakdown[num].append("Day1":"")

		for item in breakdown2:
			if (item >= float(getStart) and item <= float(getStart)+float(getHours)):
				change = {item: 1}
				breakdown.append(change)
				grid[num].append(1)
				
			else:
				change = {item: 0}
				breakdown.append(change)
				grid[num].append(0)
		

		
		for item in breakdown2:

			# print(breakdown[count][item])
			if breakdown[count][item] == 0 and precount == 0:
				startTime = 0
			elif breakdown[count][item] == 1 and precount == 0:
				startTime = breakdown2[count]
				precount = 1
			elif breakdown[count][item] == 1 and precount == 1:
				endTime = breakdown2[count]

			count += 1
		
		days[num] = {'start': startTime, 'end': endTime, 'length': (endTime-startTime)}


	# print(startTime)
	# print(endTime)

	# print(days)	
	# print(grid)

	#print(breakdown)
	#print(breakdown2)

	return(days,grid, breakdown, breakdown2)

def breaks(days, grid):

	numDays = len(grid)
	# print(numDays)
	# print(grid)
	# print(days)
	breaksList = []
	temp=[]

	yesNo = 'q'
	while (yesNo.lower() != 'y' and yesNo.lower() != 'n'):
		yesNo = str(input("Are there any scheduled breaks or meals? (y/n) "))

	if (yesNo[0].lower() == 'y'):

		
		for num in range(0,int(numDays)):
			getBreaks = int(input("How many breaks on day #"+str(num+1)+"? "))
			if (getBreaks == ''):
				getBreaks = 1
			#breaks.append(int(getBreaks))

			temp = []

			for number in range(0, (getBreaks)):
				theBreak = float(input("How long is the #"+str(number+1)+" break? "))
				temp.append(theBreak)

			breaksList.append(temp)

	if (yesNo[0].lower() == 'n'):
		for num in range (0, int(numDays)):
			breaksList.insert(num, 0)

	print(breaksList)

	return(breaksList)

def openClose(days, grid):

	

	yesNo = 'q'
	while (yesNo.lower() != 'y' and yesNo.lower() != 'n'):
		yesNo = str(input("Is there an opening ceremony/introduction/etc. attended by all? (y/n) "))

	if (yesNo[0].lower() == 'y'):

		
		getOpen = float(input("How long is this session? "))
		if (getOpen == ''):
			getOpen = .5

	if (yesNo[0].lower() == 'n'):
		getOpen = 0
		
	yesNo = 'q'
	while (yesNo.lower() != 'y' and yesNo.lower() != 'n'):
		yesNo = str(input("Is there an closing ceremony/awards/etc. attended by all? (y/n) "))

	if (yesNo[0].lower() == 'y'):

		getClose = float(input("How long is this session? "))
		if (getClose == ''):
			getClose = .5			
	
	if (yesNo[0].lower() == 'n'):
		getClose = 0	

	ceremony = {'open': getOpen, 'close': getClose}

	return ceremony

def main():
		
	#print ("test")
	rooms, capacity = getRooms()

	#print(rooms[:])
	#print(capacity[:])
	days, grid, breakdown, breakdown2 = setSchedule()
	breaksList = breaks(days, grid)
	ceremony = openClose(days, grid)
	showSchedule(rooms, capacity, days, grid, breaksList, ceremony, breakdown, breakdown2)


def showSchedule(rooms, capacity, days, grid, breaksList, ceremony, breakdown, breakdown2):

	print('\n')
	convertTime = {}
	timeList = []
	timelist2 = [':00', ':15', ':30', ':45']
	chkBreak = []

	# for num in range (0,24):
	# 	for item in timelist2:
	# 		print(str(num)+str(item))

	print(grid)

	for num in range(0, 24):
		for item in timelist2:
			timeList.append(str(num)+str(item))
		
	# for i in range(0,len(grid))	:
	# 	convertTime = {breakdown[i] : timeList[i] }

		if (len(breaksList[0]) >0 ):


			for i in range(0,len(grid)):
			
				print('DAY '+str(i+1))

				for num in range (0, len(breaksList)):

					for numb in range (0, len(breaksList[num])):

						chkBreak.append(float(breaksList[num][numb]/4))

				print(chkBreak)

				for x in range(0, len(grid[i])):
				
			# 	#print(grid[i])

				# for y in range(0, len(breaksList)): 
					
			# 		print(breaksList[x][y])

			# 	# 	chkBreak[x].append(breaksList[y]/4)

				#print(chkBreak)

					if (grid[i][x] > 0):
						print(timeList[i], '\t', grid[i][x])

		else:
			return

main()



