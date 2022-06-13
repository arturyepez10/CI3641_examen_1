# ------------------------ IMPORTS ----------------------------- #
import unittest

# locals
from TDiagrams import models, handler

# ------------------------ SUITE ----------------------------- #
class TestModels(unittest.TestCase):
  
  def testCreateProgram(self):
    ''''[SUCCESS] Puedo crear un programa'''
    p = models.Program('Test', 'LOCAL')

    self.assertSequenceEqual([p.name, p.language], ['Test', 'LOCAL'])

  def testPassProgramString(self):
    ''''[SUCCESS] Un programa tiene metodo para pasar a string'''
    p = models.Program('Test', 'LOCAL')

    self.assertEqual(str(p), 'programa \'Test\', ejecutable en \'LOCAL\'')

  def testCreateInterpreter(self):
    ''''[SUCCESS] Puedo crear un interprete'''
    i = models.Interpreter('LOCAL', 'C')

    self.assertSequenceEqual([i.base, i.language], ['LOCAL', 'C'])

  def testPassInterpreterString(self):
    ''''[SUCCESS] Un interprete tiene metodo para pasar a string'''
    i = models.Interpreter('LOCAL', 'C')

    self.assertEqual(str(i), 'interprete para \'C\', escrito en \'LOCAL\'')

  def testCreateTranslator(self):
    ''''[SUCCESS] Puedo crear un traductor'''
    t = models.Translator('LOCAL', 'C', 'JAVA')

    self.assertSequenceEqual([t.base, t.origin, t.destination], ['LOCAL', 'C', 'JAVA'])

  def testPassTranslatorString(self):
    ''''[SUCCESS] Un traductor tiene metodo para pasar a string'''
    t = models.Translator('LOCAL', 'C', 'JAVA')

    self.assertEqual(str(t), 'traductor de \'C\' hacia \'JAVA\', escrito en \'LOCAL\'')

class TestHandler(unittest.TestCase):
  def testPassAddProgram(self):
    ''''[SUCCESS] Puedo agregar un programa a la lista de programas'''
    tHandler = handler.TDiagramHandler()
    tHandler.addProgram('Test', 'LOCAL')

    self.assertSequenceEqual([len(tHandler.programs), tHandler.programs[0].name, tHandler.programs[0].language], [1, 'Test', 'LOCAL'])

  def testPassAddTranslator(self):
    ''''[SUCCESS] Puedo agregar un traductor a la lista de traductores'''
    tHandler = handler.TDiagramHandler()
    tHandler.addTranslator('LOCAL', 'C', 'JAVA')

    self.assertSequenceEqual(
      [len(tHandler.translators), tHandler.translators[0].base, tHandler.translators[0].origin, tHandler.translators[0].destination],
      [1, 'LOCAL', 'C', 'JAVA']
    )
  
  def testPassAddInterpreter(self):
    ''''[SUCCESS] Puedo agregar un interprete a la lista de interpretes'''
    tHandler = handler.TDiagramHandler()
    tHandler.addInterpreter('LOCAL', 'C')

    self.assertSequenceEqual(
      [len(tHandler.interpreters), tHandler.interpreters[0].base, tHandler.interpreters[0].language],
      [1, 'LOCAL', 'C']
    )

  def testFailAddExistingProgram(self):
    ''''[FAIL] No puedo agregar un programa que ya existe'''
    tHandler = handler.TDiagramHandler()
    tHandler.addProgram('Test', 'LOCAL')
    
    try:
      tHandler.addProgram('Test', 'LOCAL')
    except Exception as e:
      self.assertEqual(str(e), 'Ya existe el programa.')

  def testPassCanExecuteProgram(self):
    ''''[SUCCESS] Puedo ejecutar un programa en un lenguaje ejecutable'''
    tHandler = handler.TDiagramHandler()
    tHandler.addProgram('Test', 'LOCAL')

    self.assertTrue(tHandler.is_executable('Test'))

  def testFailCanExecuteProgram(self):
    ''''[FAIL] No puedo ejecutar un programa en un lenguaje no ejecutable'''
    tHandler = handler.TDiagramHandler()
    tHandler.addProgram('Test', 'JAVA')

    self.assertFalse(tHandler.is_executable('Test'))

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  unittest.main()