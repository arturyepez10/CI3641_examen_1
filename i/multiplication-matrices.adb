-- MULTIPLICACION DE MATRICES PREGUNTA 1-(b) ii
-- Arturo Yepez 15-11551
 
--  Cuerpo del modulo
package body Multiplicacion_Matrices is
  -----------------------------------------------------------
  -------------- "*" (operador de matrices) -----------------
  --  Pametros:
  -- Left: Matriz a multiplicar
  -- Right: Matriz a multiplicar
  -- --------------------------------------------------------
  -- Retorno: Matriz resultado de la multiplicacion
  -----------------------------------------------------------
  function "*" (Left, Right : Matrix) return Matrix is
    -- Se crea una matriz donde se guarda el resultado de la multiplicacion
    Result : Matrix(Left'Range(1), Right'Range(2)) := (others =>(others => 0.0));
  begin
    -- Verificacion de que las matrices sean de la misma dimension
    -- caso contrario, se levanta una excepcion
    if Left'Length(2) /= Right'Length(1) then
        raise Constraint_Error;
    end if;

    -- Aplicacion de la formula de la multiplicacion de matrices (basado en la sumatoria)
    for I in Left'range(1) loop
        for J in Right'range(2) loop
          for K in Left'range(2) loop
              Result(I,J) := Result(I,J) + Left(I, K)*Right(K, J);
          end loop;
        end loop;
    end loop;
    return Result;
  end "*";
end Multiplicacion_Matrices;
