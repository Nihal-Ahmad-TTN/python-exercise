#importing StringIO from the io module
from io import StringIO

#initialising the StringIO
file = StringIO()

#writing "Hello World" in the file
file.write("Hello world")

#setting the position of cursor at 0
file.seek(0)

#reading the content of the file
print(file.read())
