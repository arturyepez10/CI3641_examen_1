-- K-ESIMO MODULO PREGUNTA 1-(b) i
-- Arturo Yepez 15-11551

--  Cuerpo del modulo
package body K_MOD_MODULE is
  -----------------------------------------------------------
  -------------- "*" (operador de matrices) -----------------
  --  Pametros:
  -- A: Matriz a multiplicar
  -- B: Matriz a multiplicar
  -- B: Matriz a multiplicar
  -- --------------------------------------------------------
  -- Retorno: Resultado
  -----------------------------------------------------------
  function kMod (A, C : Natural; B : BiggerNatural) return Natural is
    -- Declaracion de variables
    Alt_A : Natural := A;
    Alt_B : BiggerNatural := B;
    Alt_C : Natural := C;

    Result : Natural := 1;
  begin
    if Alt_B = 0 then
      return Result;
    else
      Result := ((Alt_A mod Alt_C) * kMod(A => Alt_A, B => Alt_B - 1, C => Alt_C)) mod Alt_C;
    end if;
  end kMod;
end K_MOD_MODULE;
