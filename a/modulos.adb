-- EJEMPLO DE USO ADA PARA PREGUNTA 1-(a) ii
-- Arturo Yepez 15-11551

-- Como se importan paquetes
with Ada.Text_IO; use Ada.Text_IO;

-- Ejemplo de implementacion de Modulo en ADA (no accesible desde otras parte del codigo, como p.e. quien importa el modulo)
package body Week is
  -- Con la firma de la funcion, se puede elaborar el procedimiento a ejecutar
  procedure getFirstDay
  is begin
    -- Como usamos el `use Ada.Text_IO;` ahora todos sus metodos son accesibles sin la firma del modulo
    Put_Line ("First day of the week is " & Mon);

    -- Alternativamente, en caso de no haber usado el `use Ada.Text_IO;`, podriamos sencillamente decir
    Ada.Text_IO.Put_Line ("First day of the week is " & Mon);
  end getFirstDay;

end Week;