# ------------------------ IMPORTS ----------------------------- #
# libraries
from cmd import Cmd
from textwrap import dedent
import os
import re

# locals
from TDiagramHandler import TDiagramHandler
from utils.constants import *

# ------------------------ REPL ----------------------------- #
class TDiagramCMD(Cmd):
  """Intérprete de línea de comandos para la REPL del manejador de Diagramas T.
    
  Aplica los métodos principales para la REPL de TDiagramHandler. Utiliza los métodos
  base de Cmd, personalizados para ofrecer las funcionalidades especificadas.
  
  Atributos:
    handler: Instancia del manejador de Diagramas T.
  """

  prompt = f'{GREEN}$> {RESET}{BOLD}'

  # Mensajes de la REPL
  intro = (f'¡Bienvenido al manejador de Diagramas T!\n'
    'Utiliza "?" para mostrar los comandos disponibles.')
  doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
    'para informacion detallada)')
  misc_header = ('''Lista de funciones disponibles (escribe 'help '''
    '''<nombre>' para informacion detallada)''')

  def __init__(self):
    # Llama el constructor de la superclase e inicializa TDiagramHandler
    Cmd.__init__(self)
    self.handler = TDiagramHandler()

  # -------------- MÉTODOS QUE ENVIAN A TDIAGRAMHANDLER --------------
  def send_definir(self, command: str):
    """Envía un comando a TDiagramHandler.

    El manejador procesa la entrada y define segun el tipo requerido, o indica error en caso de haber.
    """
    # Variable donde se guarda el resultado de la accion a realizar
    result = ''

    # Debemos ver que se esta definienddo
    if self.match_command('PROGRAMA', command):
      arguments = command[8:].strip().split(' ')

      # Verificamos que el numero de argumentos sea el correcto
      if len(arguments) == 2:
        try:
          # Agregamos el programa mediante el manejador
          program = self.handler.addProgram(arguments[0], arguments[1])

          result = 'Se definio el ' + str(program)
        except ValueError:
          result = 'ERROR: Ya existe un programa llamado \'' + arguments[0] + '\'.'
      else:
        result = 'ERROR: numero incorrecto de argumentos para el tipo <PROGRAMA>.'

    elif self.match_command('TRADUCTOR', command):
      arguments = command[9:].strip().split(' ')

      # Verificamos que el numero de argumentos sea el correcto
      if len(arguments) == 3:
        # Agregamos el traductor mediante el manejador
        translator = self.handler.addTranslator(arguments[0], arguments[1], arguments[2])

        result = 'Se definio un ' + str(translator)
      else:
        result = 'ERROR: numero incorrecto de argumentos para el tipo <TRADUCTOR>.'

    elif self.match_command('INTERPRETE', command):
      arguments = command[10:].strip().split(' ')

      # Verificamos que el numero de argumentos sea el correcto
      if len(arguments) == 2:
        # Agregamos el interprete mediante el manejador
        interpreter = self.handler.addInterpreter(arguments[0], arguments[1])

        result = 'Se definio un ' + str(interpreter)
      else:
        result = 'ERROR: numero incorrecto de argumentos para el tipo <INTERPRETE>.'

    # Imprimimos por salida estandar el resultado
    self.handle_output(result)

  def send_ejecutable(self, command: str):
    """Envía un comando al manejador de diagramas T.

    El manejador procesa la entrada e indica si ese programa -en caso de existir- puede ser ejecutable, o
    indica error en caso de haber.
    """
    pass


  # -------------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL --------------
  def help_definir(self):
    print(dedent('''
      Aplica el manejador de Diagramas T, para definir un <tipo>.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del manejador de Diagramas T. En caso de error, se le notifica al usuario el problema.

      Los tipos disponibles para definir son:
      - PROGRAMA
      - TRADUCTOR
      - INTERPRETADOR

      Cada tipo tiene sus propios argumentos a ser tomados en cuenta.

      Su ejecucion se realiza mediante:
      >>> DEFINIR <tipo> [<argumentos>]'''))

  # TODO: cambiar texto
  def help_ejecutable(self):
    print(dedent('''
      Aplica el manejador del Buddy System para liberar memoria ya reservada.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del Buddy System. En caso de error, se le notifica al usuario el problema.

      Su ejecucion se realiza mediante:
      >>> EJECUTABLE <nombre>'''))

  # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------
  def cmdloop(self, intro = None):
    """Ver clase base. Agrega manejo de interrupciones del teclado."""
    print(self.intro)
    while True:
      try:
        super(TDiagramCMD, self).cmdloop(intro='')
        break
      except KeyboardInterrupt:
        self.handle_output(f'\n(Para salir, utiliza el comando SALIR o escribe .)')

  def do_exit(self, line: str) -> bool:
    """Finaliza el CMD/REPL del manejador de diagramas T. Retorna True.
    
    Se puede ejecutar de dos maneras:
      >>> exit
      >>> SALIR
    """
    return True

  def do_clear(self, line: str):
    """Limpia la pantalla de la terminal de los comandos anteriores."""
    command = 'clear'

    # Si el SO es Windows, cambia el comando
    if os.name in ('nt', 'dos'):
      command = 'cls'
    os.system(command)

  def emptyline(self) -> bool:
    """Procesador de lineas en blanco. Retorna False.
    
    El comportamiendo por defecto es no hacer nada.
    """
    return False

  def default(self, line: str) -> None:
    """Procesador de entrada por defecto.

    Retorna:
      True si se termina la ejecucion del manejador de diagramas T.
      None cuando se interpreta un comando e imprime su salida.
    """

    if self.match_command('SALIR', line):
      return self.do_exit(line)
    elif self.match_command('DEFINIR', line):
      command = line[7:].strip()
      self.send_definir(command)
    elif self.match_command('EJECUTABLE', line):
      command = line[10:].strip()
      self.send_ejecutable(command)
    else:
      self.handle_output('ERROR: comando no reconocido (\'' + line + '\').')

  # -------------- MISCELÁNEA --------------
  def handle_output(self, line: str, color: str = BLUE, end = '\n'):
    """Imprime con un color en específico los resultados de la REPL al
    usuario.
    """
    # Si es un error, se imprime de rojo y se guarda la tupla con información
    if line.startswith('ERROR:'):
      color = RED

    print(f'{RESET}{color}{line}{RESET}', end=end)

  def match_command(self, name: str, line: str) -> bool:
    '''Retorna un booleano indicando si la línea contiene un comando.
    
    Argumentos:
      name: Nombre del comando.
      line: Línea a analizar.
    '''
    return bool(re.match(f'{name}($| )', line, re.IGNORECASE))
