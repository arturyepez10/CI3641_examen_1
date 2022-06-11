# ------------------------ PROGRAMA ----------------------------- #
class Program:
  """Representacion del modelo de 'Programa', segun su diseño en Diagramas T.
  
  Atributos y Parametros:
    name: Nombre que representa al programa.
    language: lenguaje de programacion en el que esta escrito el programa.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, name: str, language: str):
    self.name = name
    self.language = language.upper()

  # -------------- DEFINICION DE STRINGS --------------
  def __str__(self) -> str:
    return 'programa \'' + self.name + '\', ejecutable en \'' + self.language + '\''

# ------------------------ TRADUCTOR ----------------------------- #
class Translator:
  """Representacion del modelo de un 'Traductor' de lenguajes de programacion, segun su diseño en Diagramas T.
  
  Atributos:
    base: Lenguaje de programacion en el que esta escrito el traductor.
    origin: Lenguaje de programacion del que traduce.
    destination: Lenguaje de programacion al que traduce.

  Parametros:
    base_language: Lenguaje de programacion en el que esta escrito el traductor.
    origin_language: Lenguaje de programacion del que traduce.
    destination_language: Lenguaje de programacion al que traduce.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, base_language: str, origin_language: str, destination_language: str):
    self.base = base_language
    self.origin = origin_language
    self.destination = destination_language

  def __str__(self) -> str:
    return 'traductor de \'' + self.origin + '\' hacia \'' + self.destination +'\', escrito en \'' + self.base + '\''

# ------------------------ INTERPRETADOR ----------------------------- #
class Interpreter:
  """Representacion del modelo de un 'Interprete' de lenguajes de programacion, segun su diseño en Diagramas T.
  
  Atributos:
    base: Lenguaje de programacion en el que esta escrito el interprete.
    language: Lenguaje de programacion que interpreta.

  Parametros:
    base_language: Lenguaje de programacion en el que esta escrito el interprete.
    language: Lenguaje de programacion que interpreta.
  """
  # -------------- CONSTRUCTOR --------------
  def __init__(self, base_language: str, language: str):
    self.base = base_language
    self.language = language

   # -------------- DEFINICION DE STRINGS --------------
  def __str__(self) -> str:
    return 'interprete para \'' + self.language + '\', escrito en \'' + self.base + '\''