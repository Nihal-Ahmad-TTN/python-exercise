import program

from importlib import reload
while True:
    program.hello()
    reload(program)
