'''
Question:
You have a number.txt, with each line a real number. 
Write a code to split this file into 3 files as follows: 
even.txt -- contain all even numbers 
odd.txt -- all odd number 
float.txt -- all floating point number 
Use with() clause for file handling
'''

#opening the number.txt file in read mode
with open("number.txt",'r') as file:

    #iterating the mines of the file
    for num in file:

        #checking if the number is int type
        if "." not in num:

            #checking if the number is even
            if int(num)%2==0:
                #writing the number in even.txt file
                with open("even.txt",'a') as even:
                    even.write(num)

            else:
                #writing the number in odd.txt file
                with open("odd.txt",'a') as odd:
                    odd.write(num)
        

        else:
            #writing the float numbers in float.txt file
            with open("float.txt",'a') as float:
                float.write(num)
