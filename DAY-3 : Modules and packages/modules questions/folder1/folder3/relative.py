#Importing the contents of file1.py and file2.py file using relative import
from .file2 import hello
from ..folder2.file1 import hi

hello()
hi()