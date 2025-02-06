'''
Question:
Can we sort a dictionary? Why or why not? 

Answer:
Yes , we can sort a dictionary. We can use the following method to display the sorted value of the dictionary using the keys of the given dictionary.
'''

names={"Nihal": 29, "Rohit": 30, "Naman": 16, "Rishabh": 50, "Ahaan": 34}
keys=list(names.keys())
keys.sort()
for name in keys:
    print(name,":",names[name])