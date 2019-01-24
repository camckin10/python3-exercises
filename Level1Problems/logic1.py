#CodingBat Python logic 1 problems

#problem 1
#cigar_party--A squirrel party is successful when the number of cigars is between 40 & 60 inclusive. Unless it is the weekend, in which case there is no upperbound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. 

def cigar_party(cigars, is_weekend):
	if cigars == 40 and cigars == 60:
		return True
	elif cigars < 40 and cigars > 60:
		return True
	else:
		return False 


#2nd solution
def cigar_party(cigars, is_weekend):
	if is_weekend:
		return True
	elif cigars >= 40 and cigars <= 60:
		return True
	else:
		return False 

	#problem 2
	#date_fashion--You and  your care try to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10 and the "date" is the stylishness of your dates clothes. The result getting the table is encoded as an int value with 0 = no, 1 = maybe, 2= yes. If either of you is very stylish, 8 or more, the result is 2(yes). With the exception that either of you has style of 2 or less, then the result is 0(no). Otherwise, the  result is 1(maybe). 
	#date_fashion(5,10) --> 2 

	def date_fashion(you, date):
		if you != 8 or date == 8:
			return 2
		elif you >= 2 and date <= 2:
			return O
		elif you < 8 and date > 8 :
			return 1 

	def date_fashion(you, date):
		if you >= 2 and date >= 8:
			return 0
		elif you < 8 and date < 8 :
			return 1 
		elif you > 8 and date < 8 :
			return 2
		else:
			return 'Testing, testing, 1,2,3'

	#problem 3 
	#squirrel_play--Squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise. 
	#squirrel_play(70, False)--> True

	#temp 60 -90 reg. seasons
	#temp 60 - 100 summer

	def squirrel_play(temp, is_summer):
		if is_summer:
			return True
		#temps between 60-100
		elif temp <=90 and temp >= 60:
			return True
		else:
			return False

	#problem 4
	#caught_speeding--You are driving too fast, and a police office stops you. Write code to computer the result, encoded as an int value: 
	#0 = no ticket, 1 = small ticket, 2 = big ticket
	#if speed is 60 or less,the result is 0. Speed between 61-80 inclusive, the result is 1. If speed if 81 or more, the result is 2. Unless it is your birthday, on that day, your speed can be higher in all cases. 
   
	#0 = no ticket --speed 60 or less
	#1 = small ticket -- speed 61-80
	#2 = big ticket -- speed 81 or more
	#Birthday -- all speeds add +5 

	def caught_speeding(speed, is_birthday):
		if is_birthday:
			return speed + 5
		elif speed <= 60:
			return 0 
		elif speed >= 80 or speed <= 61:
			return 1
		elif speed >= 81:
			return 2
		else:
			return False 


	#problem 5 
	#sorta_sum--Given 2 ints, a and b, return their sum. However, sums in range 10..19 inclusive, are forbidden, so in that case just return 20. def sorta_sum(3,4)-->7

	def sorta_sum(a,b):
		sum = a + b 
	if a >= 10 and b<= 19:
		return sum
	elif a <=10 or b <= 10:
		return sum
	else:
		return False 

	def sorta_sum(a,b):
		sum = a + b
	if sum in range(10,19):
		return 20
	elif a <= 10 or b <= 10:
		return sum
	elif a >= 10 and b <= 19:
		return sum
	else:
		return False 

	#problem 6
	#alarm_clock--Given a day of the week encoded as: 0 = Sun  1 = Mon 2 = Tue...6 = Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm shoud be "7:00" and of the weekend it should be "10:00". Unless we are on vacation--then on weekdays it should be "10:00" and weekends it should be "off". 
	
	#0 = Sun
	#1 = Mon ("7:00")
	#2 = Tues ("7:00")
	#3 = Wed  ("7:00")
	#4 = Thurs ("7:00")
	#5 = Fri ("7:00")
	#6 = Sat -- "10:00"

	def alarm_clock(day, vacation):
		if day == vacation:
			return "10:00"
		elif day >= 1 and day <= 6:
			return "7:00"
		else:
			return "off"

	def alarm_clock(day, vacation):
		if day == vacation:
			return "10:00"
		elif day > 1 and day < 6:
			return "7:00"
		else:
			return "off"
		
		#problem 7
		#love6--The number 6 is a truly great number: Given 2 int values, a and b, return True if either on is 6. Or, if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number

		def love6(a,b):
			if a and b == 6:
				return True
			elif a == b or b == 6:
				return True
			else:
				return False 

		def love6(a,b):
			if a + b or a - b == 6:
				return True
			elif a == 6  or b == 6:
				return True
			else:
				return True 

	
	#problem 8
	#in1to10--Given a number n, return True if n is in the range 1...10 inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

	def in1to10(n, outside_mode):
		n --> range 1..10 --> True
		outside_mode --> True --> n <= 1 or n >= 10

	def in1to10(n,outside_mode):
		if outside_mode:
			return True
		elif n in range(1,10):
			return True
		else:
			return False 


	#problem 9
	#near_ten--given a non-negative number "num", return True if num is within 2 or a multiple of 10. Note:(a % b) is the remainder of dividing a by b, so (7%5) is 2. 
	#near_ten(12)->True   near_ten(17)--False

	def near_ten(num):
		if num % 2 == 10:
			return True
		elif num % 2 == 0:
			return True
		else:
			return False

	def near_ten(num):
		if num % 2 == 10 or num %2 >= 10:
			return True
		else:
			return False 
