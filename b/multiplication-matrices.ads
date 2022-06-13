-- MULTIPLICACION DE MATRICES PREGUNTA 1-(b) ii
-- Arturo Yepez 15-11551

-- Firma del modulo que contiene la funciones para la multiplicacion de matrices
package Multiplicacion_Matrices is
  type Matrix is array (Natural range <>, Natural range <>) of Float;

  --  Se define como un operador aritmetico
  function "*" (Left, Right : Matrix) return Matrix;
end Multiplicacion_Matrices;
