"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Follow up: Could you solve it without converting the integer to a string?
"""


def isPalindrome(x):
	reversed_num = 0
	number = x
	if x < 0:
		return False
	while x > 0:
		digit = x % 10
		reversed_num = reversed_num * 10 + digit
		x //= 10

	return number == reversed_num


print(isPalindrome(121))











