-- EJEMPLO DE USO ADA PARA PREGUNTA 1-(a) iii
-- Arturo Yepez 15-11551

-- Importamos un paquete al que queremos asignarle un alias
with Ada.Text_IO;

procedure Main is
  -- Renombramos el paquete `Ada.Text_IO` como `TIO`
  package TIO renames Ada.Text_IO;
begin
  TIO.Put_Line ("Hello");
end Main;
