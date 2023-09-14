


"""
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

def solve(string):
    dict = {}
    for i in string:
        keys = dict.keys()
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
print(solve("google.com"))





