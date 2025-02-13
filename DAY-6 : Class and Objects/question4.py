class MathOperations:
    # creating a function that accepts two compulsary and one optional parameter
    def add(self, num1, num2, num3 = 0): 
        return num1 + num2 + num3
    

# making of the instance of the class
addition=MathOperations()

#passing two numbers
result1= addition.add(1, 2)
print(result1) 

#passing 3 numbers
result2= addition.add(1, 2, 3)
print(result2)