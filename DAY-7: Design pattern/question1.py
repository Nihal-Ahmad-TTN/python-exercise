'''
Write an object oriented code to implement Prime number class.

Implement a Prime class which should have following funcnatinality:

- Ability to test if a number is prime or not 
- Generate prime numbers
- Generate prime numbers greater than a number N
- Generate prime numbers  less than a number N
- Generate all prime numbers between N, to M
- implement __len__() to tell number of primes between N and M where N < M

-  overload +, += operators to nerate number prime number with respect to current prime  nuber  e.g.

>> p = Prime(3)
>> p + 1
5
>> p + 2
7
>> p += 3
>> p
Prime(11)

implement `__repr__()`  and `__str__() methods
'''

#Defining the class prime
class prime:

    #initialising
    def __init__(self, number=2):
        self.number=number
        
    #function to check if the number is prime or not
    def checkprime(self, number=0):
        if number==0:
            number=self.number
        for num in range(2, int(self.number**0.5)):
            if number%num==0:
                return False
        return True

    #function to generate prime numbers from starting
    def generateprime(self, start=2, stop=9999):
        for num in range(start, stop+1):
            for divider in range(2, int(num**0.5)+1):
                if num%divider==0:
                    break
            else:
                yield num
    
    #function to generate prime numbers greater than N
    def largeprime(self, start=0, stop=9999):
        if start==0:
            start=self.number
        for num in range(start, stop+1):
            for divider in range(2, int(num**0.5)+1):
                if num%divider==0:
                    break
            else:
                yield num

    #function to generate prime numbers smaller than N
    def lessprime(self, stop=9999, start=2):
        if stop==9999:
            stop=self.number
        prime=[]
        for num in range(start, stop+1):
            for divider in range(2, int(num**0.5)+1):
                if num%divider==0:
                    break
            else:
                prime.append(num)
        return prime
    
    #function to generate prime numbers between N and M (M>N)
    def inbetweenprime(self, start, stop):
        self.prime=[]
        for num in range(start, stop+1):
            for divider in range(2, int(num**0.5)+1):
                if num%divider==0:
                    break
            else:
                self.prime.append(num)
        return self.prime
    
    #function to overload +
    def __add__(self, other):
        result=self.largeprime(self.number)
        for num in range(other-1):
            next(result)
        return next(result)
    
    #function to overload +=
    def __iadd__(self, other):
        result=self.largeprime(self.number)
        for i in range(other-1):
            next(result)
        self.number= next(result)
        return prime(self.number)

    #function to return the length of prime numbers between N nd M (M>N)
    def __len__(self):
        return len(self.prime)
    
    #function to override __str__()
    def __str__(self):
        return "string"
    
    #function to override __repr__()
    def __repr__(self):
        return "repr"

#creating object
prime_obj=prime(100)

#calling checkprime() without any argument
print(prime_obj.checkprime())
print()

#calling checkprime() to check prime number 11
print(prime_obj.checkprime(11))
print()

#calling checkprime() to check non-prime number 12
print(prime_obj.checkprime(12))
print()

#generating first 5 prime numbers from 2
result=prime_obj.generateprime()
for number in range(5):
    print(next(result))
print()

#generating first 5 primenumbers greater than N which is passed in object creation
result=prime_obj.largeprime()
for number in range(5):
    print(next(result))
print()

#generating first 5 primenumbers greater than 20
result=prime_obj.largeprime(20)
for number in range(5):
    print(next(result))
print()

#generating first 5 primenumbers smaller than N which is passed in object creation
result=prime_obj.lessprime()
print(result)
print()

#generating first 5 primenumbers smaller than 20
result=prime_obj.lessprime(20)
print(result)
print()

#generating primenumbers between 10, 30
result=prime_obj.inbetweenprime(10,30)
print(result)
print()

#checking number of prime numbers between 10, 30
prime_obj.inbetweenprime(10,30)
print(len(prime_obj))
print()

#checking the overloading of +
print(prime_obj+1, prime_obj+3, prime_obj+2)
print()

#checking the overloading of +=
prime_obj+=5
print(prime_obj)
print()
print(next(prime_obj.largeprime()))
print()

#printing __str__() of object
print(prime_obj.__str__())
print()

#printing __repr__() of object
print(prime_obj.__repr__())
print()