# ------------------------ BUDDY SYSTEM ----------------------------- #
class BuddySystem:
  """Representacion del 'Buddy System', que es un modelo de manejo y asignacion de memoria.

  La particularidad es que el Buddy System es que realiza el manejo de memoria en numeros 
  con base dos (2^n). 
  
  Por ejemplo, tener que guardar 3 bloques de data, resulta en que se le asigne 4 bloques (2^2) de
  memoria disponible para guardar la informacion. Tiene como imprevisto que se tiene a poseer mayor
  fragmentacion interna, en vez de externa.
  
  Atributos:
    space: Arreglo que simboliza la cantidad de memoria inicializada.
    blocks: Arreglo que resume los fragmentos de bloques de memoria disponible.

  Parametros:
    init_space: cantidad de bloques de memoria a crear/manejar.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, init_space: int) -> None:
    '''Constructor de clase.'''

    # Inicializamos los arreglos que representaran a la memoria
    self.total_memory = init_space
    self.total_free_memory = init_space
    self.blocks_summary = [{ 'name': '', 'size': init_space, 'real_size': init_space, 'isFree': True, 'starts_in': 0 }]

  # -------------- METODOS DE CLASE --------------
  def allocate(self, name: str, size: int) -> str:
    '''Maneja la reserva de memoria.'''

    # Encontramos cuanta memoria debe reservarse
    allocation_qty = self.nearest_block(size)

    # Mensaje Resultados
    result = 'Memoria reservada de forma exitosa (' + str(size) + ' -> ' + str(allocation_qty) +' bloques).'

    # Verificamos que el nombre no este tomado ya
    if self.block_exists(name):
      return 'ERROR: el nombre (' + name + ') ya esta asignado a otro bloque de memoria.'

    # Asignamos memoria
    if self.total_free_memory < allocation_qty:
      result = 'ERROR: no existe suficiente memoria libre para la cantidad asignada (' + str(size) + ' -> ' + str(allocation_qty) +' bloques).'
    else:
      # Indice del arreglo de bloques en el cual se va a comenzar la memoria reservada
      insertion_index = -1

      # Buscamos un bloque de memoria libre que tenga al menos la cantidad necesitada
      for index, block in enumerate(self.blocks_summary):
        if (block['isFree'] and block['size'] >= allocation_qty):
          insertion_index = index
      
      if insertion_index != -1:
        # Direccion donde comienza el bloque de memoria reservador
        starts = self.blocks_summary[insertion_index]['starts_in']

        # Si es la cantidad completa del bloque, reemplazamos la informacion
        if self.blocks_summary[insertion_index]['size'] == allocation_qty:
          self.blocks_summary[insertion_index]['name'] = name
          self.blocks_summary[insertion_index]['real_size'] = size
          self.blocks_summary[insertion_index]['isFree'] = False
        else:
          # Le restamos al bloque existente en esa posicion original el 'size' y la direccion donde comienza
          self.blocks_summary[insertion_index]['size'] -= allocation_qty
          self.blocks_summary[insertion_index]['real_size'] -= allocation_qty
          self.blocks_summary[insertion_index]['starts_in'] += allocation_qty

          # Insertamos el nuevo bloque
          self.blocks_summary.insert(insertion_index, { 'name': name, 'size': allocation_qty, 'real_size': size, 'isFree': False, 'starts_in': starts })

        # Actualizamos la cantidad total de memoria disponible
        self.total_free_memory -= allocation_qty
      else:
        result = 'ERROR: no existe un bloque contiguo de memoria disponible (' + str(size) + ' -> ' + str(allocation_qty) +' bloques).'

    return result

  def free(self, name: str) -> str:
    '''Maneja la liberacion de memoria.'''

    # Encontramos el indice del elemento que debemos eliminar
    deletion_index = self.get_block_index(name)

    # Mensaje Resultados
    result = ''

    if deletion_index is not None:
      # Cantidad de memoria liberada
      freed_memory = self.blocks_summary[deletion_index]['size']

      # Debemos liberar la memoria y a su vez, verificar si tiene memoria libre a sus lados
      # Si es el primer elemento y el de posterior esta libre
      if deletion_index == 0 and self.blocks_summary[deletion_index + 1]['isFree']:
        self.blocks_summary[deletion_index + 1]['size'] += self.blocks_summary[deletion_index]['size']
        self.blocks_summary[deletion_index + 1]['real_size'] += self.blocks_summary[deletion_index]['size']
        self.blocks_summary[deletion_index + 1]['starts_in'] = self.blocks_summary[deletion_index]['starts_in']

        # Eliminamos el primer bloque
        self.blocks_summary.pop(deletion_index)

      # Si es el ultimo elemento y el anterior esta libre
      elif deletion_index == (len(self.blocks_summary) - 1) and self.blocks_summary[deletion_index - 1]['isFree']:
        self.blocks_summary[deletion_index - 1]['size'] += self.blocks_summary[deletion_index]['size']
        self.blocks_summary[deletion_index - 1]['real_size'] += self.blocks_summary[deletion_index]['size']

        # Eliminamos el primer bloque
        self.blocks_summary.pop(deletion_index)

      # Si es un elemento del medio y alguno de sus lados estan libres
      elif self.blocks_summary[deletion_index - 1]['isFree'] or self.blocks_summary[deletion_index + 1]['isFree']:
        # Verificamos si solo el lado derecho esta libre
        if self.blocks_summary[deletion_index + 1]['isFree'] and not self.blocks_summary[deletion_index - 1]['isFree']:
          self.blocks_summary[deletion_index + 1]['size'] += self.blocks_summary[deletion_index]['size']
          self.blocks_summary[deletion_index + 1]['real_size'] += self.blocks_summary[deletion_index]['size']
          self.blocks_summary[deletion_index + 1]['starts_in'] = self.blocks_summary[deletion_index]['starts_in']

        # Verificamos si solo el lado izquierdo esta libre
        elif self.blocks_summary[deletion_index - 1]['isFree'] and not self.blocks_summary[deletion_index + 1]['isFree']:
          self.blocks_summary[deletion_index - 1]['size'] += self.blocks_summary[deletion_index]['size']
          self.blocks_summary[deletion_index - 1]['real_size'] += self.blocks_summary[deletion_index]['size']

        # Si ambos lados estan libres
        elif self.blocks_summary[deletion_index - 1]['isFree'] and self.blocks_summary[deletion_index + 1]['isFree']:
          self.blocks_summary[deletion_index - 1]['size'] += ( 
            self.blocks_summary[deletion_index]['size'] + self.blocks_summary[deletion_index + 1]['size']
          )
          self.blocks_summary[deletion_index - 1]['real_size'] += (
            self.blocks_summary[deletion_index]['size'] + self.blocks_summary[deletion_index + 1]['size']
          )

          # Eliminamos el elemento posterior
          self.blocks_summary.pop(deletion_index + 1)

        # Eliminamos el elemento
        self.blocks_summary.pop(deletion_index)

      else:
        self.blocks_summary[deletion_index]['name'] = ''
        self.blocks_summary[deletion_index]['real_size'] = self.blocks_summary[deletion_index]['size']
        self.blocks_summary[deletion_index]['isFree'] = True
  
      result = 'Memoria liberada de forma exitosa (' + str(freed_memory) +' bloques).'
    else:
      result = 'ERROR: No existe ningun bloque de memoria con el nombre (\'' + name + '\').'

    return result

  def show(self) -> dict[str, any]:
    '''Maneja el resumen de datos de la memoria.'''

    # General information
    data = {
      'total_memory': self.total_memory,
      'total_free_memory': self.total_free_memory,
      'memory_blocks': self.blocks_summary
    }
    
    return data

  # -------------- MISCELÁNEA --------------
  # TODO: check case when x == 1
  def nearest_block(self, x: int) -> int:
    """Encuentra la potencia de 2 mas cercana al numero que recibe por entrada.

    Por ejemplo, la potencia de 2 mas cercana a 65 es 128 == (2^7)
    """
    return 0 if x == 0 else 2**(x - 1).bit_length()

  def block_exists(self, name: str) -> bool:
    """Encuentra -si existe- un bloque de memoria reservado con ese nombre.
    """
    exists = False

    # Iteraciones sobre el arreglo de bloques
    for block in self.blocks_summary:
      if block['name'] == name:
        exists = True
        break
    
    return exists

  def get_block_index(self, name: str) -> bool:
    """Encuentra -si existe- un bloque de memoria reservado con ese nombre.

    Retorno:
      index: Indice donde se encuentra el bloque de memoria por liberar
    """
    index = None

    # Iteraciones sobre el arreglo de bloques
    for i, block in enumerate(self.blocks_summary):
      if block['name'] == name:
        index = i
        break
    
    return index