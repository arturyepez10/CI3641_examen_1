# ------------------------ IMPORTS ----------------------------- #
# libraries
from sys import argv

# locals
from shell import TDiagramCMD

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  enter = True

  if len(argv) == 1:
    repl = TDiagramCMD()

    repl.cmdloop()
  else:
    raise ValueError('Cantidad invalida de parametros.')