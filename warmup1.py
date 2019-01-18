#warmup1 problems from coding bat
#problems will feature how many tests passed, other solutions, etc. 

#problem 1
#diff 21--Given an int n, return absolute difference between n and 21, except
#return double the absolute difference if n is over 21. 
def diff21(n):
	if n<21:
		return n * 2
	else:
		return (n-21)

#second solution to problem 1
def diff21(n):
	if n <= 21:
		return 21-n
	else:
		return(n-21)*2


#problem 2
#parrot trouble--The hour parameter is the current hour in range 0...23. 
#The parrot is trouble if the parrot is talking, and the hour is before
#7 or after 20. Return true if parrot is in trouble.

def parrot_trouble(talking,hour):
	if hour > 7 and hour < 20:
		return True
	else:
		return False 

#problem 3
#makes10--Given two ints, a and b, return True if one of them is 10, or their sum is 10.

#first solution
def makes10(a,b):
	if a + b == 10:
		return True
	elif a - b == 10:
		return True
	else:
		return False

#second solution
def make10(a,b):
	if a+b == 10:
		return True
	elif a -b == 10:
		return True
	elif b + a == 10
	  return True
	elif b - a == 10:
		return True
	else:
		return False


#problem 4
#near_hundred--Given an int n, return True if it is within 10 of 100 or 200. Note:abs(num) computes the absolute value of a number

def near_hundred(n):
	if n > 90 and 190:
		return False
	else:
		return True 



#problem 5 
#pos_neg--Given two int values, return True is one if negative and one is positive. 
#Except if parameter "negative" is True, return True only if both are negative.

def pos_neg(a,b,negative):
	if a == b or a > b :
		return True
	elif negative == "negative":
		return True
	else:
		return False

#problem 6
#not_string- Given a string, return a new string with "not" in front of it. However, if string already has "not", return unchanged. 

def not_string(str):
	if str == "not" str:
		return True
	elif "not" str == "not" str:
		return False
#PLEASE NOTE: I did not solve this problem yet.
#Below is the solution given by the site.

#site solution
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3


	#problem 7
	#sleep_in--Parameter weekday is True if it is a weekday, parameter vacation is True if we are on vacation. We sleep in if it is NOT a weekday and we're on vacation. Return True if we sleep in. 

	#weekday = True - not on vacation
	#vacaction = True - not a weekday
	#sleep_in = True - on vacation

	def sleep_in(weekday,vacation):
		weekdays = ["Mon", "Tues", "Wed","Thurs","Fri"]
		if weekday != vacation:
			return True
		elif vacation:
			return True

		#second solution
		def sleep_in(weekday,vacation):
			if weekday != vacation:
				return True
			elif weekday == weekday:
				return True
			else:
				return False 

#problem 8 
#monkey trouble-We have 2 monkeys, a and b, and the parameters a_smile and b_smile indicate if each if smiling. We are in trouble if both are smiling or if neither of them are smiling. Return True if we are in trouble

def monkey_trouble(a_smile, b_smile):
	if a_smile and b_smile:
		return True
	elif not a_smile and not b_smile:
		return True
	else:
		return False 

	#problem 9
	#sum_double--Given two int values, return their sum. Unless the two values are the same, then return double their sum.

	def sum_double(a,b):
		a= 5   num = 0 
		b = 10 sum = 0
		if a + b:
			return num
		if a == a and b == b:
			return a * 2 and b * 2
		else:
			return False

			#second solution
			def sum_double(a,b):
				if a + b = sum:
					return sum
				elif a == b:
					return a * 2 and b * 2
				else: 
					return False

  #problem 10
	#missing_char- Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string(i.e. n will be in the range 0..len(str)-1 inclusive)

	#whew this one was a doozy!

	def missing_char(str,n):
		if str == 5
		 print(str[:0])
		elif str < 2:
			print(str[:1])
		elif str == 3:
			print(str[:1])
		else:
			return null

	#problem 11
	#front_back- Given a string, return a new string where the first and last  chars have been exchanged. 

	def front_back(str):
		front_char = str[:-1]
		back_char = str[:0]
		return str 

		def front_back(str):
			front_char = str[:0]
			back_char = len(str[-1:])
			return str
		
	#problem 12
	#front3--Given a string, we'll say that the front is the front 3 chars of the string. if the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

	def front3(str):
		str = str
		if len(str) < 4;
			return str * 3
		elif len(str) > 4:
			return str * 3

	def front3(str):
		if len(str) < 4 or len(str) > 4:
			return str *3

	def front3(str):
		if len(str) <= 4:
			return str *3
		else:
			return null
			
	def front3(str):		
		first_chars = str[:3]
		return first_chars * 3



