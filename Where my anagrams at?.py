# Kata link : https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    fin = []
    for i in words:
        if sorted(i) == sorted(word):
            fin.append(i)
    return fin
    
#print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
