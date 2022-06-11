# ------------------------ IMPORTS ----------------------------- #
# locals
from models import Program, Translator, Interpreter

# ------------------------ HANDLERS ----------------------------- #
class TDiagramHandler:
  """Representacion del manejador de Diagramas T, para lenguajes de programacion.

  Este manejador se encarga de aplicar los metodos necesarios para poner hacer asociaciones entre
  los programas, traductores e interpretes. A su vez, podra manejar definiciones de nuevos tipos y
  utilizarlas para el manejo de estos
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self) -> None:
    self.programs = []
    self.translators = []
    self.interpreters = []

  # -------------- INICIALIZADORES --------------
  def addProgram(self, name: str, language: str) -> Program:
    '''Crea un nuevo programa y lo agrega a la lista de programas.
    '''
    # Revisamos si ya existe un programa con ese nombre
    filtered = filter(
      lambda p: p.name == name,
      self.programs
    )
    if len(list(filtered)) > 0:
      raise ValueError('Ya existe el programa.')
    
    # Nuevo programa
    p = Program(name=name, language=language)

    # Lo agregamos a la lista de programas
    self.programs.append(p)

    return p

  def addTranslator(self, base_language: str, origin_language: str, destination_language: str) -> Translator:
    '''Crea un nuevo traductor y lo agrega a la lista de traductores.
    '''

    # TODO: check if already exists (no obligatorio)
    
    # Nuevo traductor
    t = Translator(base_language=base_language, origin_language=origin_language, destination_language=destination_language)

    # Lo agregamos a la lista de traductores
    self.translators.append(t)

    return t

  def addInterpreter(self, base_language: str, language: str) -> Interpreter:
    '''Crea un nuevo interpretador de lenguage y lo agrega a la lista de lenguajes.
    '''

    # TODO: check if already exists (no obligatorio)
    
    # Nuevo traductor
    i = Interpreter(base_language=base_language, language=language)

    # Lo agregamos a la lista de traductores
    self.interpreters.append(i)

    return i