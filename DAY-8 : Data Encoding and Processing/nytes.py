#initialising
str = "Hello"

#encoding the strings into bytes
byte = str.encode("utf-8")
print(byte)

#decoding the bytes into utf-8
str = byte.decode("utf-8")
print(str)

#creating a bytearray
bytearr = bytearray([68, 69, 70])
print(bytearr)