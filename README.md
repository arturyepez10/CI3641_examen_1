# EXAMEN 1 | CI3641
### Arturo Yepez 15-11551

## Descripcion del Examen

Para el examen se requirio que algunas de las preguntas fuera programa. Para ello, las condiciones fueron que se llevaran a cabo en un repositorio de GitHub y fuera compartido con el profesor.

El grupo de preguntas que debian de ser resueltas mediante una solucion de programacion, fueron:

1. (1-a) Dado el lenguaje elegido para trabajar, se mostraron algunos ejemplos de `modulos`, importar y exportar nombres; a su vez algunos ejemplos de alias y sobrecarga.
2. (1-b) Se debian de implementar los siguientes programas:
  i. La k-esima potencia de un numero.
  ii. La multiplicacion de dos matrices.
3. (3) Modelado e implementacion de un programa que simule un manejador de memoria que utilice el *"Buddy System"*.
4. (4) Modelado e implementacion, de un modulo en un lenguaje de programacion que defina el tipo cuaternion y permita la operaciones de:
  i. Suma de cuaterniones, y de constantes.
  ii. Conjugada de cuaterniones.
  iii. Multiplicacion de cuaterniones y de constantes.
  iv. Valor absoluto de cuaterniones.
5. (5) En base a lo visto en clases, modelar e implementar un programa que simule a los *Diagramas T*, utiles para asociaciones entre programas, interpretadores y traductores.

## Respuestas

Las respuestas fueron alojadas en diferentes ramas del repositorio. Las ramas disponibles son:

- `pregunta-1`: Contiene la solucion a las preguntas 1(a) y 1(b).
- `pregunta-3`: Contiene la solucion a la pregunta 3.
- `pregunta-4`: Contiene la solucion a la pregunta 4.
- `pregunta-5`: Contiene la solucion a la pregunta 5.

En cada una de las ramas, se pueden encontrar los archivos que forman su respectiva respuesta y ademas, en este mismo archivo se extiende para presentar una descripcion del problema, detalles de la implementacion y formas de uso.

---

## MODULO DE CUATERNIONES

Para esta pregunta se utilizo el lenguaje de programacion `Python`[^1].

Dado que necesitabamos una forma de poder interactuar exclusivamente entre cuaterniones, se decidio modelar el tipo `Cuaternion` como una clase.

La razon principal por la que se decidio modelar el tipo `Cuaternion` como una clase fue porque las clases se utilizan para modelar objetos, en los cuales podemos sobrecargar (o definir) operaciones, como lo fueron las siguientes: suma (`+`), producto (`*`), valor absoluto (`+ _`) y conjugada (`~`).

Ahora, una vez definidas esas operaciones de esa forma el lenguaje permite utilizar los operadores aritmeticos asocioados a las operaciones sin necesidad de directamente llamar a ninguna funcion.

Asi entonces, el uso de la libreria en el mismo lenguaje va de la siguiente manera:
```
# Importamos la libreria
from Cuaterniones import Cuaternion

# Definimos valores/instancias de cuaterniones de la siguiente forma
a = Cuaternion(1, 0, 0, 0)
b = Cuaternion(0, 1, 0, 0)

# Podemos operar de forma aritmetica
print('Suma de cuaterniones: ', a + b)
print('Suma de un escalar: ', a + 1)
print('Conjugada: ', ~a)
print('Productos de cuaterniones: ', a * b)
print('Producto de cuaternion por escalar: ', a * 2)
print('Valor absoluto: ', +a)
```

[^1]: Nota: Inicialmente se planteo como un modulo para Haskell, pero luego de algunos problemas que no pudieron ser solucionados por cuestion de tiempo, se decidio que se utilizara el lenguaje de programacion `Python` para lograr llegar a una solucion definitva. Se puede checar la carpeta `alternativo/`