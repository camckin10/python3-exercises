#Level2 Python3 Problems

#Problem 1- make_bricks
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

#small = 1 inch   big = 5 inches  goal = ??

#12 out of 30 tests
def make_bricks(small,big,goal):
	if small and big == goal:
		return True
	else:
		return False 

#Problem 2- lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

#only 1 test passed
def lone_sum(a,b,c):
	sum = a + b + c 
	if a == a or b == b:
		return c 
	elif c == c or b == b:
		return a 
	elif c == c or a == a :
		return b 
	else:
		return sum 

#9 out of 10 tests corrects--more than half
def lone_sum(a,b,c):
	sum = a + b + c
	if a == b == c:
		return False
	elif a == b:
		return c
	elif b == c:
		return a 
	elif c == a:
		return b 
	else:
		return sum 

#Problem 3 - lucky_sum
#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

#3 out of 13 tests passed
def lucky_sum(a,b,c):
	if a == 13 or b == 13:
		return c + a 
	elif c == 13:
		return a + b 
	else:
		return False 

# 7 out of 12 tests passed
def lucky_sum(a,b,c):
	wrong_value = 12
	sum = a + b + c    
	if a == wrong_value:
		return b + c     
	elif b  == wrong_value:   
		return a + c       
	elif c == wrong_value:
		return a + b       
	else:
		return sum 

#no tests passed
def lucky_sum(a,b,c):
	if a == b == c == 13:
		return False
	else:
		return True 


#Problem 4 - no_teen_sum
#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

#5 out of 17 tests passed
def no_teen_sum(a,b,c):
	sum = a + b + c   
	if a in range(13,19):
		return sum
	elif b == 15 or c == 16:
		return sum 
	else:
		return sum 

#5 out of 17 tests passed
def no_teen_sum(a,b,c):