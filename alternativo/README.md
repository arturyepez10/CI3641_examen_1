## MODULO DE CUATERNIONES (`Haskell`)

Para esta pregunta se utilizo el lenguaje de programacion `Python`[^1].

Dado que necesitabamos una forma de poder interactuar exclusivamente entre cuaterniones, se decidio modelar el tipo `Cuaternion` como un `typeclass` de la forma`data`.

La razon principal por la que se decidio modelar el tipo `Cuaternion` como `typeclass` fue para aprovechar la sobrecarga de operadores de Haskell, de tal forma que pudieramos interectuar con la instancia `Num Cuaternion` y definir nuestras operaciones.

Ahora, una vez definidas las operaciones de esa forma el lenguaje permite utilizar los operadores aritmeticos asociados a las operaciones sin necesidad de directamente llamar a ninguna funcion.

Asi entonces, el uso de la libreria en el mismo lenguaje va de la siguiente manera:
```
-- Importamos la libreria
from Cuaterniones import Cuaternionimport Cuaterniones ( Cuaternion ( Cuaternion ) )

-- Definimos valores/instancias de cuaterniones de la siguiente forma
a = Cuaternion 1 0 0 0
b = Cuaternion 0 1 0 0

-- Podemos realizar operaciones utilizando aritmetica

-- Suma de Cuaterniones
print ( a + b )

-- Suma de escalar
print ( a + 1 )

-- Conjugada
print ( -a )

-- Multiplicacion de Cuaterniones
print ( a * b )


-- Multiplicacion de escalar por un cuaternion
print ( a * 2 )

-- Valor absoluto no implementado
```

### Problematica

Una de las razones por la que `Haskell` fue dejado de lado para el paso de su implementacion en `Python` fue debido al dominio del lenguaje. El primero es uno que no se maneja del todo bien, y surgieron tres (3) problemas:

1. La definicion inicial fue hecha en base a `Integer`, dado que no se encontro la forma de representar que fuera cualquier tipo de numero.
2. No se pudo implementar la funcion `abs` de `Num Cuaternion` tal que se pudiera asignar un operador unario mas alla de la misma frase `abs`, y ademas, no se encontro una solucion al problema de tipo de retorno, dado que la instancia exigia retornar un `Cuaternion` cuando debia de ser un numero por definicion.
3. No se logro sobrecargar los operadores para obtener para obtener la respuesta en el formato exigido.

Por esas razones, se decidio optar por `Python` para la solucion de los problemas.