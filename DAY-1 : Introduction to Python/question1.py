'''
Question:

Write a Python script to test if a number is prime or not? 
- The Script name: primes.py 
- Add a functions is_prime() which return boolean True or False 
- Program should accept a number from console

'''
def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        return True

num=int(input("Enter the number : "))
if is_prime(num):
    print("Number is prime")
else:
    print("Number is not prime")
