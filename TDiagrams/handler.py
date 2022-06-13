# ------------------------ IMPORTS ----------------------------- #
# locals
from .models import Program, Translator, Interpreter

# ------------------------ HANDLERS ----------------------------- #
class TDiagramHandler:
  """Representacion del manejador de Diagramas T, para lenguajes de programacion.

  Este manejador se encarga de aplicar los metodos necesarios para poner hacer asociaciones entre
  los programas, traductores e interpretes. A su vez, podra manejar definiciones de nuevos tipos y
  utilizarlas para el manejo de estos
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self) -> None:
    self.programs : list[Program] = []
    self.translators : list[Translator] = []
    self.interpreters : list[Interpreter] = []
    self.executable_languages = ['LOCAL']

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
    
    # Nuevo traductor
    t = Translator(
      base_language=base_language,
      origin_language=origin_language,
      destination_language=destination_language
    )

    # Lo agregamos a la lista de traductores
    self.translators.append(t)

    # Verificamos si se genera un lenguaje ejecutable
    self.update_executable_languages()

    return t

  def addInterpreter(self, base_language: str, language: str) -> Interpreter:
    '''Crea un nuevo interpretador de lenguage y lo agrega a la lista de lenguajes.
    '''
    
    # Nuevo traductor
    i = Interpreter(base_language=base_language, language=language)

    # Lo agregamos a la lista de traductores
    self.interpreters.append(i)

    # Verificamos si se genera un lenguaje ejecutable
    self.update_executable_languages()

    return i

  # -------------- EJECUCION --------------
  def is_executable(self, program_name: str) -> bool:
    '''Verifica si un programa es ejecutable en la maquina.
    '''
    # Buscamos si existe un programa con ese nombre
    program = None
    for p in self.programs:
      if p.name == program_name:
        program = p
        break
    
    if program is None:
      raise ValueError('No existe un programa con ese nombre.')

    else:
      # Se vuelve a verificar los lenguaje ejecutables
      self.update_executable_languages()

      # Buscamos si el lenguaje en el que esta escrito es ejecutable
      for exec_lang in self.executable_languages:
        if exec_lang == program.language:
          return True
      return False

  # -------------- MISCELÁNEA --------------
  def update_executable_languages(self):
    '''Actualiza la lista de lenguajes ejecutables.
    '''
    # Nuevos lenguajes ejectuables
    new_exec_lang = []

    # --------- Verificamos si los interpretes generan lenguajes ejectuables
    for interpreter in self.interpreters:
      # Vemos todos los lenguajes ejecutables
      for exec_lang in self.executable_languages:
        # Si el lenguaje en el que esta escrito el interprete es ejecutable, 
        # entonces el lenguaje interpretado puede ejecutarse
        if exec_lang == interpreter.base:
          new_exec_lang.append(interpreter.language)

    # Actualizamos la lista de lenguajes ejectuables
    for new_exec in new_exec_lang:
      if new_exec not in self.executable_languages:
        self.executable_languages.append(new_exec)

    # --------- Verificamos si los traductores generan lenguajes ejecutables
    new_exec_lang = []

    for translator in self.translators:
      # Si el traductor es ejecutable y el lenguaje generado ejecutable, el lenguaje de origen es ejecutable
      if (translator.base in self.executable_languages) and (translator.destination in self.executable_languages):
        new_exec_lang.append(translator.origin)

    # Actualizamos la lista de lenguajes ejectuables
    for new_exec in new_exec_lang:
      if new_exec not in self.executable_languages:
        self.executable_languages.append(new_exec)

