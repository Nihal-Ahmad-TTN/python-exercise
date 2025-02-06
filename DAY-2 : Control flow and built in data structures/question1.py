'''
Question:
Write a code to filter all sub-strings which have an even number of vowels?
'''

str= "I have an input string which contains even and odd numbers of vowels aA aa aaa ae aeo"
str=str.split(' ')
vowels=['a','e','i','o','u']
for words in str:
    count=0
    for char in words:
        if char.lower() in vowels:
            count+=1
    if count%2==0:
        print(words)
