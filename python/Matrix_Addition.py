#!/bin/python3

#Kata link : https://www.codewars.com/kata/526233aefd4764272800036f/train/python
#Title : Matrix Addition

'''
sample output

|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|

'''
# Program to add two matrices using nested loop

def matrix_addition(a, b):
    result = a
    final = []
    for i in range(len(a)):
	    for j in range(len(a[0])):
		    result[i][j] = a[i][j] + b[i][j]
    for r in result:
    	final.append(r)
    return final

print(matrix_addition(X,Y))

