'''
Question:
Reassign 'hello' in this nested list to say 'goodbye' instead: 
list3 = [1,2,[3,4,'hello']] 
'''


list3 = [1,2,[3,4,'hello']] 
print("Before replacement : ", list3)
list3[2][2]='goodbye'
print("After replacement : ", list3)