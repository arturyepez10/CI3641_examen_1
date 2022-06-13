-- K-ESIMO MODULO PREGUNTA 1-(b) i
-- Arturo Yepez 15-11551

-- Firma del modulo que contiene la funciones para el k-esimo modulo
package K_MOD_MODULE is
  subtype BiggerNatural is Integer range 2..Integer'Last;

  --  Se define como un operador aritmetico
  function kMod (A, B : Natural; C : BiggerNatural) return Natural;
end K_MOD_MODULE;
