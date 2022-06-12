-- EJEMPLO DE USO ADA PARA PREGUNTA 1-(a) ii
-- Arturo Yepez 15-11551

-- Ejemplo de firma de Modulo en ADA, que es la encargada de exportar
package Week is
  -- Variable privada, inacessible desde fuera del paquete
  private AllDays : constant String := "Monday Tuesday Wednesday Thursday Friday Saturday Sunday";

  -- Variables publicas, accesibles desde fuera del paquete
  Mon : constant String := "Monday";
  Tue : constant String := "Tuesday";
  Wed : constant String := "Wednesday";
  Thu : constant String := "Thursday";
  Fri : constant String := "Friday";
  Sat : constant String := "Saturday";
  Sun : constant String := "Sunday";

  -- Aqui va la firma de los metodos existentes en el paquete
  procedure getFirstDay;
end Week;