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
