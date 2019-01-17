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
