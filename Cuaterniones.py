# ------------------------ IMPORTS ----------------------------- #
# libraries
from math import sqrt
from numbers import Number

# ------------------------ OBJETO PRINCIPAL ----------------------------- #
class Cuaternion:
  """Representacion de los cuaterniones.

  La forma general de cuaternión se define como:
    a + b.i + c.j + d.k, para a, b, c, d ∈ R
  
  
  Atributos y Parametros:
    a: Numero real, de la parte real del cuaternion.
    b: Numero real, coeficiente de una parte imaginaria del cuaternion (i).
    c: Numero real, coeficiente de una parte imaginaria del cuaternion (j).
    d: Numero real, coeficiente de una parte imaginaria del cuaternion (k).
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, a: Number, b: Number, c: Number, d: Number):
    '''Constructor de clase.'''
    if (isinstance(a, Number) and isinstance(b, Number) and isinstance(c, Number) and isinstance(d, Number)):
      self.a = a
      self.b = b
      self.c = c
      self.d = d
    else:
      raise TypeError('Los argumentos deben ser numericos.')

  def __str__(self) -> str:
    '''Representacion en cadena de caracteres.'''

    # Si los numeros tienen longitud distinta de 1, se rodean en parentesis
    a = self.a if len(str(self.a)) == 1 else '(' + str(self.a) + ')'
    b = self.b if len(str(self.b)) == 1 else '(' + str(self.b) + ')'
    c = self.c if len(str(self.c)) == 1 else '(' + str(self.c) + ')'
    d = self.d if len(str(self.d)) == 1 else '(' + str(self.d) + ')'

    return '{} + {}.i + {}.j + {}.k)'.format(a, b, c, d)

  # -------------- SOBRECARGA DE OPERADORES --------------
  def __add__(self, other):
    ''' Sobrecarga del operador suma (+).

    Permite la suma de cuaterniones, y a su vez la suma de una constante
    con un cuaternion.

    La suma esta definida como la suma de sus componentes.

    La suma de un cuartenion y un numero real es la suma de sus componentes
    con el numero real.

    Ejemplo de una operacion valida:
    >>> a = Cuaternion(1, 2, 3, 4)
    >>> b = Cuaternion(5, 6, 7, 8)
    >>> a + b === Cuaternion(6, 8, 10, 12)
    '''
    # Variables para la suma
    a, b, c, d = self.a, self.b, self.c, self.d

    # Se verifica si el otro operando es un cuaternion
    if (isinstance(other, Cuaternion)):
      a += other.a
      b += other.b
      c += other.c
      d += other.d

    # Se verifica si el otro operando es un numero real
    elif (isinstance(other, Number)):
      a += other

    else:
      raise TypeError('El operador solo puede ser usado con cuaterniones o numeros reales.')

    return Cuaternion(a ,b, c, d)

  def __invert__(self):
    b = -self.b
    c = -self.c
    d = -self.d

    return Cuaternion(self.a ,b, c, d)

  def __mul__(self, other):
    ''' Sobrecarga del operador multiplicacion (*).

    Permite la multiplicacion de cuaterniones, y a su vez la multiplicacion de una constante
    con un cuaternion.

    La multiplicacion de cuaterniones esta definida por la siguiente formula:\n
      (a1 + b1i + c1j + d1k) ∗ (a2 + b2i + c2j + d2k) = 
        (a1a2 − b1b2 − c1c2 − d1d2) +
        (a1b2 + b1a2 + c1d2 − d1c2)i +
        (a1c2 − b1d2 + c1a2 + d1b2)j +
        (a1d2 + b1c2 − c1b2 + d1a2)k

    La multiplicacion entre un cuaternion y un numero real esta dada por la multiplicacion de 
    sus componentes con el numero real.

    Ejemplo de una operacion valida:
    >>> a = Cuaternion(1, 2, 3, 4)
    >>> b = Cuaternion(5, 6, 7, 8)
    >>> a * b === Cuaternion(-26, -52, -78, -104)
    '''

    # Variables de la multiplicacion
    a, b, c, d = self.a, self.b, self.c, self.d

    # Se verifica si el otro operando es un cuaternion
    if (isinstance(other, Cuaternion)):
      a = self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d
      b = self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c
      c = self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b
      d = self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a

    # Se verifica si el otro operando es un numero real
    elif (isinstance(other, Number)):
      a *= other

    else:
      raise TypeError('El operador solo puede ser usado con cuaterniones o numeros reales.')

    return Cuaternion(a ,b, c, d)

  def __pos__(self) -> Number:
    ''' Sobrecarga del operador positivo (+).

    Se utiliza como reemplazo del operador and(&).

    Se encarga de calcular el valor absoluto de un cuaternion, dado por la
    formula:
      |a + bi + cj + dk| = sqrt(a^2 + b^2 + c^2 + d^2)

    Ejemplo de una operacion valida:
    >>> a = Cuaternion(1, 1, 1, 1)
    >>> +a === 2.0
    '''
    return sqrt(self.a ** 2 + self.b ** 2 + self.c ** + self.d ** 2)
