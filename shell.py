# ------------------------ IMPORTS ----------------------------- #
# libraries
from cmd import Cmd
from textwrap import dedent
import os
import re

# locals
from buddySystem import BuddySystem
from utils.constants import *

# ------------------------ REPL ----------------------------- #
class BuddySystemCMD(Cmd):
  """Intérprete de línea de comandos para la REPL cliente del manejador de espacio BuddySystem.
    
  Aplica los métodos principales para la REPL de BuddySystem. Utiliza los métodos
  base de Cmd, personalizados para ofrecer las funcionalidades especificadas.
  
  Atributos:
    bs: Instancia de la máquina virtual que recrea a BuddySystem.
  """

  prompt = f'{GREEN}accion => {RESET}{BOLD}'

  # Mensajes de la REPL
  intro = (f'¡Bienvenido a BuddySystem!\n'
    'Utiliza "?" para mostrar los comandos disponibles.')
  doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
    'para informacion detallada)')
  misc_header = ('''Lista de funciones disponibles (escribe 'help '''
    '''<nombre>' para informacion detallada)''')

  def __init__(self, space_qty: int):
    # Llama el constructor de la superclase e inicializa la máquina virtual
    Cmd.__init__(self)
    self.bs = BuddySystem(space_qty)

  # -------------- MÉTODOS QUE ENVIAN A BUDDY SYSTEM --------------
  def send_reservar(self, command: str):
    """Envía un comando al reservador de memoria del Buddy System.

    El reservador procesa la entrada y reserva la cantidad de memoria, o indica error en caso de haber.
    """

    try:
      # Entrada
      [name, space] = command.split(' ')

      # Manejador de memoria
      out = self.bs.allocate(name, int(space))

      self.handle_output(out)
    except ValueError:
      self.handle_output('ERROR: Incorrecto numero o tipo de argumentos.')

  def send_liberar(self, command: str):
    """Envía un comando al liberador de memoria del Buddy System.

    El liberador procesa la entrada y libera la memoria reservada bajo el nombre indicado, o indica
    error en caso de haber.
    """

    try:
      # Manejador de memoria
      out = self.bs.free(command)

      self.handle_output(out)
    except ValueError:
      self.handle_output('ERROR: Incorrecto numero o tipo de argumentos.')

  def send_mostrar(self):
    """Envía un comando al manejador de memoria del Buddy System, para mostrar una representacion grafica de la lista
    de bloques.

    El liberador procesa la entrada y muestra la informacion por la salida estandar.
    """

    # Recogemos la data que devuelve el Buddy System
    data = self.bs.show()

    # Deconstruimos los valores
    total_memory : int = data['total_memory']
    total_free_memory : int = data['total_free_memory']
    memory_blocks : list[dict[str, any]] = data['memory_blocks']

    # Show header
    self.handle_output('# ------------------------------------ #')
    self.handle_output('# RESUMEN DE USO DE BLOQUES DE MEMORIA #')
    self.handle_output('# ------------------------------------ #')
    self.handle_output('  total = ' + str(total_memory) + ' bl.', end=' | ')
    self.handle_output('libre = ' + str(total_free_memory) + ' bl.')

    self.output_memory_blocks(memory_blocks, total_memory=total_memory)

  # -------------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL --------------
  def help_reservar(self):
    print(dedent('''
      Aplica el manejador del Buddy System para reservar memoria.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del Buddy System. En caso de error, se le notifica al usuario el problema.

      Su ejecucion se realiza mediante:
      >>> RESERVAR <nombre> <espacio>'''))

  def help_liberar(self):
    print(dedent('''
      Aplica el manejador del Buddy System para liberar memoria ya reservada.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del Buddy System. En caso de error, se le notifica al usuario el problema.

      Su ejecucion se realiza mediante:
      >>> LIBERAR <nombre>'''))

  # TODO: completar
  def help_mostrar(self):
    print(dedent('''
      Imprime por salida estándar una lista de errores almacenados hasta
        el momento, en orden cronológico, con el siguiente formato:

        [
            (<ruta_a_archivo>, <línea_de_error>, <descripción_del_error>),
            (<ruta_a_archivo>, <línea_de_error>, <descripción_del_error>),
                    .                 .                     .
                    .                 .                     .
                    .                 .                     .
            (<ruta_a_archivo>, <línea_de_error>, <descripción_del_error>),
        ]
    --------------
      Aplica el manejador del Buddy System para liberar memoria ya reservada.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del Buddy System. En caso de error, se le notifica al usuario el problema.

      Su ejecucion se realiza mediante:
      >>> MOSTRAR'''))

  # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------
  def cmdloop(self, intro = None):
    """Ver clase base. Agrega manejo de interrupciones del teclado."""
    print(self.intro)
    while True:
      try:
        super(BuddySystemCMD, self).cmdloop(intro='')
        break
      except KeyboardInterrupt:
        self.handle_output(f'\n(Para salir, utiliza el comando SALIR o escribe .)')

  def do_exit(self, line: str) -> bool:
    """Finaliza el CMD/REPL de BuddySystem. Retorna True.
    
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
      True si se termina la ejecucion de la VM.
      None cuando se interpreta un comando e imprime su salida.
    """

    if self.match_command('SALIR', line):
      return self.do_exit(line)
    elif self.match_command('RESERVAR', line):
      command = line[8:].strip()
      self.send_reservar(command)
    elif self.match_command('LIBERAR', line):
      command = line[7:].strip()
      self.send_liberar(command)
    elif self.match_command('MOSTRAR', line):
      self.send_mostrar()
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
      name: Nombre del comando magico.
      line: Línea a analizar.
    '''
    return bool(re.match(f'{name}($| )', line, re.IGNORECASE))

  def output_memory_blocks(self, blocks: list[dict[str, any]], total_memory: int) -> None:
    """Imprime por salida estandar toda la informacion de los bloques de memoria que recibe
    como parametros.
    """

    # Contador de fragmentacion interna total acumulada
    total_frag = 0

    self.handle_output('')
    self.handle_output('  uso de bloques de memoria')
    self.handle_output('  -------------------------')

    # Recorremos todos los bloques de memoria
    for index, block in enumerate(blocks):
      self.handle_output('    ', end=' ')

      self.handle_output('#' + str(index) + ' | ' + str(block['starts_in']) + ' ->', end=' ')

      # Si el bloque esta libre, el output es diferente
      if block['isFree']:
        self.handle_output('LIBRE' + ' ; ' + 'memoria = ' + str(block['size']) + ' bl.')
      else:
        total_frag += block['size'] - block['real_size']
        
        # Hacemos output de la informacion del bloque
        self.handle_output(block['name'] + ' ; ' + 'memoria = ' + str(block['size']) + ' bl.', end= ' ')

        # Output de la informacion relacionada a la fragmentacion interna de este bloque de memoria
        frag = 100 - (block['real_size'] / block['size']) * 100
        self.handle_output('; frag-int = ' + str(round(frag, 2)) + '%')

    # Informamos los datos globales sobre la fragmentacion interna
    self.handle_output('')
    self.handle_output('  Fragmentacion Interna Total = ' + str(total_frag), end=' ')
    total_frag = 100 - (total_frag / total_memory) * 100
    self.handle_output('; % Fragmentacion Interna Total = ' + str(round(total_frag, 2)))