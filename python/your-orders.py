# kata link : https://www.codewars.com/kata/55c45be3b2079eccff00010f/

def order(sentence):
    ans = []
    for i in range(1,len(sentence)):
        for j in sentence.split():
            if str(i) in j:
                ans.append(j)
    return ' '.join([i for i in ans])
    
'''
SOLUTION WITH USING DICTIONARIES

def order(sentence):

    sentence = sentence.split(' ')
    key = {}
    for i in sentence:
        for j in i:
            if j.isnumeric() == True:
                key[j] = i
    ff = sorted(key)
    ans = ''
    for i in ff:
        ans += key[i] + ' '
    
    return ans[:-1]
'''
