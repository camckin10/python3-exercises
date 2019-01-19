#CodingBat List 1 Python Problems

#problem 1
#first_last6 -- Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be the length of 1 or more. 
#first_last6([1,2,6])-- True   first_last6([13,4,24])-- False

def first_last6(nums):
	if len(nums) == 6:
		return True
	else:
		return False

	def first_last6(nums):
		if nums[-1:] or nums[:-1] == 6:
			return True
		else:
			return False

	def first_last6(nums):
		if nums[0] and nums[len(nums)-1] == 6:
			return True
		else:
			return False 

	#problem 2 
	#secure_first_last--Given an array of ints return True if the array is length of 1 or more, and the 1st element and the last element are equal. 

	def same_first_last(nums):
		nums = []
		if len(nums) == len(nums):
			return True
		elif nums[0] and num[len(nums)-1] == nums:
			return True
		else:
			return False 

	#problem 3
	#make_pi--Return an int array length 3 containing the last 3 digits of pi{3,1,4}.

	def make_pi():
		pi = [3,1,4]
		return pi 
	
	#ALL TESTS CORRECT :) 

	#problem 4
	#common_end--Given 2 arrays of ints, a and b, return True if they have the same 1st element or have the same last element. Both arrays will be length 1 or more. 

	def common_end(a,b):
		if a == b:
			return True
		elif a[0] == b[0]:
			return True
		elif a[:-1] and b[:-1] == True
			return True
		else:
			return False 

	def common_end(a,b):
		if a == b:
			return True
		elif a[0] == b[0]:
			return True
		else:
			return False 

	#problem 5 
	#sum3--Given an array of ints length 3, return the sum of all the elements.

	def sum3(nums):
		sum_result = (sums(nums))
		return sum_result

	#problem 6 
	#rotate_left3--Given an array of ints length 3, return an array with the elements "rotated left" so {1,2,3} yields {2,3,1}. 

	def rotate_left3(nums):
		return [nums[1], nums[2], nums[0]]

		def rotate_left3(nums):
			return nums[1:] + nums[:1] 

	#problem 7
	#reverse3--Given an array of ints length 3, return order, so {1,2,3} becomes {3,2,1}

	def reverse3(nums):
		nums.reverse()
		return nums

	#problem 8
	#max_end3--Given an arry of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array. 

	def max_end3(nums):
		max1 = max(nums[0], nums[-1])
		return [max1, max1, max1]

	def max_end3(nums):
		m = max(nums[0], nums[2])
		return [ m, m, m]

	#problem 9 
	#3