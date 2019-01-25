#CodingBat Python String1 Problems

#problem 1
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

#no tests passed for either problem...hmmmmm....
def hello_name(name):
	return "Hello" + name + "!"

def hello_name(name):
	name = " " message = "Hello"
	return message + name + "!"

#problem 2
#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

#all tests passed using both solutions

def make_abba(a,b):
	return a + b * 2 + a 

def make_abba(a,b):
	return a + b + b + a 


#problem 3
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

#correct for 4 out of 8 tests
def make_tags(tag,word):
	tag1 = "<i>"
	tag2 = "</i>"
	return tag1 + word + tag2

#correct for 4 out of 8 tests
def make_tags(tag,word):
	return "<i>" + word + "</i>"

#problem 4
#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

#correct for 2 out of 6 tests
def make_out_word(out,word):
	return "<<" + word + ">>"

#problem 5


