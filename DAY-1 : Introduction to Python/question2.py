'''
Question:
Write a code to print binary, octal or hexa-decimal presentation of a number. Do not use any third party library.

'''

def binary(num):
	bin=""
	while(num>0):
		bin=bin+str(num%2)
		num=num//2
	return bin[::-1]
	
def octal(num):
	oct=""
	while(num>0):
		oct=oct+str(num%8)
		num=num//8
	return oct[::-1]

def hexadecimal(num):
	mapping={
		10 : "A",
		11 : "B",
		12 : "C",
		13 : "D",
		14 : "E",
		15 : "F"}
	hexa=""
	while(num>0):
		res=num%16
		if(res>9):
			hexa=hexa+str(mapping[res])
		else:
			hexa=hexa+str(res)
		num=num//16
	return hexa[::-1]


num=int(input("Enter a number to print its binary, octal and hexadecimal representation : "))
if num==0:
	print("Binary Representation : 0")
	print("Octal Representation : 0")
	print("Hexadecimal Representation : 0")
else:
	print("Binary Representation : ",binary(num))
	print("Octal Representation : ",octal(num))
	print("Hexadecimal Representation : ",hexadecimal(num))

