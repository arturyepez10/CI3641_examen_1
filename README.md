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

## Diagramas T

Para esta pregunta se utilizo el lenguaje de programacion `Python`.


Dado que el ejercicio requiere una interfaz que permita de forma interactiva ingresar comandos, se hizo la implementacion utilizando principios del paradigma de programacion orientado a objetos. Donde, entre las librerias de `Python`, se encuentra una que se puede utilizar para simular una `CMD` o `SHELL` al correr el script, totalmente personalizable[^note].

Luego, se crearon tres modelos de datos tal que representen a los *Diagramas T* (ubicado en `models.py`):
- `Program`, simulando a un programa definido en una computadora.
- `Interpreter`, simulando a un interprete de lenguajes de programacion.
- `Translator`, simulando a un traductor de lenguajes de programacion.

Luego, tenemos una _"Clase padre"_ que maneja el uso de los modelos de datos para simular las operaciones y/o asociaciones entre ellos. Entre las caracteristicas de esta clase, se encuentran:
- Lleva un recuento de todos los programas, interpretes y traductores creados.
- Permite verificar si un programa es ejecutable o no.
- Luego de cada operacion, se corre una subrutina que crea las conexiones entre los modelos de datos. Tal que, en caso de encontrar un nuevo __"lenguaje ejecutable"__, lo agrega a una lista que lleva la cuenta. Esto simplifica la verificacion de los programas ejecutables en un lenguaje en especifico, dado que no se debe verificar todas las asociaciones cada vez que se introduce el comando `EJECUTAR` sino solo una vez, ya sea cuando se agregue el traductor o interprete que termine de detectar; si se detecta un lenguaje ejecutable nuevo, se agrega a la lista.

Para correr el programa, simplemente hay que ejecutar el siguiente comando desde el directorio del repositorio:
```
python run.py
```

Esto da inicio al simulador de `REPL`, donde se pueden utilizar los comandos descritos en los requerimientos del programa.

[^note]:
    En el REPL, todos los comandos son ajenos a __"case insensitive"__.

[^note]:
    Si te sientes agobiado por la cantidad de informacion, prueba a utilizar el comando `clear` :)

[^note]:
    Si quieres conocer la documentacion de un comando, simplemente escribe `help <comando>` en el REPL, o `help`/`?` para conocer la lista de comandos.
