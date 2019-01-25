#CodingBat Python String1 Problems

#problem 1-hello_name
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

#no tests passed for either problem...hmmmmm....
def hello_name(name):
	return "Hello" + name + "!"

def hello_name(name):
	name = " " message = "Hello"
	return message + name + "!"

#problem 2--make_abba
#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

#all tests passed using both solutions

def make_abba(a,b):
	return a + b * 2 + a 

def make_abba(a,b):
	return a + b + b + a 


#problem 3--make_tags
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

#correct for 4 out of 8 tests
def make_tags(tag,word):
	tag1 = "<i>"
	tag2 = "</i>"
	return tag1 + word + tag2

#correct for 4 out of 8 tests
def make_tags(tag,word):
	return "<i>" + word + "</i>"

#problem 4--make_out_word
#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

#correct for 2 out of 6 tests
def make_out_word(out,word):
	return "<<" + word + ">>"

#problem 5--extra_end
 #Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

#correct for 2 out of 6 tests
 def extra_end(str):
	 return str * 3
 
#another solution found through github?
 def extra_end(str):
	 str_result = str[-2:] * 3
	 return str_result 

#problem 6--first_two
#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

#correct for 2 out of 9 tests
def first_two(str):
	if str >= 2:
		return str[:-2]
	elif str <= 2:
		return str
	else:
		return False 

#all tests correct
def first_two(str):
	if str <= 2 or str == " ":
		return str
	else:
		return str[:2]
	
#problem 7--first_half
#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

#correct for 4 out of 8 tests
def first_half(str):
	if len(str) == len(str):
		return str[:3]
	else:
		return False 

#correct for 4 out of 8 tests
def first_two(str):
	if len(str) == len(str) or len(str) >= 3:
		return str[:3]
	else:
		return [len(str)]

#problem 8--without_end
#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

#correct for 3 out of 9 tests
def without_end(str):
	if len(str) == len(str) or len(str) != len(str):
		return str[1:3]

#All tests correct AND a gold star
def without_end(str):
	if len(str) == len(str) or len(str) != len(str):
		return str[1:-1]


#problem 9--combo_string
#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

#correct for 6 out of 12 tests
def combo_string(a,b):
	if len(a) <= 3 or len(a) == 0:
		return a + b + a 
	elif len(b) >= 3:
		return a + b + a 
	else:
		return False 

#correct for 7 out of 12 tests
def combo_string(a,b):
	if len(a) <= 3 or len(a) == 0 :
		return a + b + a
	elif len(b) <= 3 or len(b) == 0 :
		return b + a + b
	else:
		return False 

#problem 10-non_start
#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

#correct for 6 out of 12 tests
def non_start(a,b):
	if len(a) <= 3 or len(a) == 0 :
		return [1:] + b [1:]
	else:
		return False 

#all tests correct
def non_start(a,b):
	if a == a and b == b :
		return a[1:] + b [1:]

#problem 11- left2
#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

#1 out of 9 test passed
def left2(str):
	if len(str) >= 2:
		return str[-2:]
	else:
		return False 

#all tests passed 
def left2(str):
	return str[2:] + str[:2]


	






