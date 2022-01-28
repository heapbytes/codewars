#!/bin/python3

#Kata link : https://www.codewars.com/kata/5266876b8f4bf2da9b000362/
#Title : Who likes it?


'''
Sample Output

	test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
'''


def likes(names):
	if len(names)==0:
		return 'no one likes this'
	elif len(names)==1:
		return names[0] + ' likes this'
	elif len(names)==2:
		return names[0] + ' and ' + names [1] + ' like this'
	elif len(names)==3:
		return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
	elif len(names)==4:
		return names[0] + ', ' + names[1] + ' and 2 others like this'
	else:
		return names[0] + ', ' + names[1] + ' and ' + str(len(names[2:])) + ' others like this' 

