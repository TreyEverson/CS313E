#  File: MagicSquare.py

#  Description:

#  Student's Name: Trey Everson

#  Student's UT EID: RHE 323
 
#  Partner's Name: Chase Kirkland

#  Partner's UT EID: CFK 348

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 9/1/19

#  Date Last Modified: 9/5/19

# This assignment was done in pair-programming

# Populate a 2-D list with numbers from 1 to n^2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
import numpy as np 


def make_square ( n ):
	# magic_square = np.zeros((n, n), dtype=int)
	magic_square = [[0 for x in range(n)] for y in range(n)] # Filling the list with zeros

	i = n / 2
	j = n - 1

	number = 1
	# Magic square algorithum, goes until the highest number is n^2
	while number <= (n * n):
		if i == -1 and j == n:
			j = n - 2
			i = 0
		else:
			if j == n:
				j = 0
			if i < 0:
				i = n -1
		if magic_square[int(i)][int(j)]:
			j = j - 2
			i = i + 1
			continue
		else:
			magic_square[int(i)][int(j)] = number
			number = number + 1
			j = j + 1
			i = i - 1
	return magic_square

# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
	n = int(len(magic_square))
	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magic_square[i][j]),end = '') # Formatting to justify the numbers
			# print(magic_square[i][j])
			if j == n - 1:
				print()

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
	n = int(len(magic_square))
	s = 0
	# Diagnal 1
	for i in range(0, n):
		s = s + magic_square[i][i]
	# Diagnal 2
	s2 = 0
	for i in range(0, n):
		s2 = s2 + magic_square[i][n-i-1]

	if s != s2:
		return False
	# Row
	for i in range(0, n):
		rowSum = 0
		for j in range(0, n):
			rowSum += magic_square[i][j]

		if rowSum != s:
			return False
	# Column
	for i in range(0, n):
		colSum = 0
		for j in range(0, n):
			colSum += magic_square[j][i]

		if s != colSum:
			return False

	return True

def main():
	# Prompt the user to enter an odd number 1 or greater
	# Check the user input
	n = int(input("Please enter an odd number: "))
	while n % 2 == 0:
		n = int(input("Please enter an odd number: "))
	# if int(n) % 2 != 0:
	# 	print("Invalid.")
		# exit()
	# Create the magic square
	magic_square = make_square(n)
	# Print the magic square
	print("\nHere is a", n, "X", n, "magic square: \n")
	print_square(magic_square)
	print("")
	# Verify that it is a magic square
	check_square(magic_square)
	if check_square(magic_square) == True:
		print("This is a magic square and the canonical sum is", int(n * (n * n + 1) / 2), "\n")
	else:
		print("This is not a magic square")
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
	main()