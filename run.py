# ------------------------ IMPORTS ----------------------------- #
# libraries
from sys import argv

# locals
from shell import BuddySystemCMD

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  enter = True

  if len(argv) == 2:
    repl = BuddySystemCMD(int(argv[1]))

    repl.cmdloop()
  else:
    raise ValueError('Necesita 1 parametros.')