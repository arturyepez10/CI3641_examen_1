# ------------------------ IMPORTS ----------------------------- #
import unittest

# locals
from MemoryHandler.buddySystem import BuddySystem

# ------------------------ SUITE ----------------------------- #
class TestMemoryHandler(unittest.TestCase):
  
  def testPassReservar(self):
    '''[PASS] Puedes reservar bloques de memoria.'''

    bs = BuddySystem(1024)
    out = bs.allocate(name='name', size=10)

    self.assertEqual(out, 'Memoria reservada de forma exitosa (10 -> 16 bloques).')

  def testFailDuplicados(self):
    '''[FAIL] No puedes reservar bloques de memoria con el mismo nombre.'''

    bs = BuddySystem(1024)
    bs.allocate(name='name', size=10)
    out = bs.allocate(name='name', size=10)

    self.assertEqual(out, 'ERROR: el nombre (\'name\') ya esta asignado a otro bloque de memoria.')

  def testFailReservarExceso(self):
    '''[FAIL] No puedes reservar bloques de memoria que excedan el tamaño total de la memoria.'''

    bs = BuddySystem(1024)
    out = bs.allocate(name='name', size=2048)

    self.assertEqual(out, 'ERROR: no existe suficiente memoria libre para la cantidad asignada (2048 -> 2048 bloques).')

  def testPassLiberar(self):
    '''[PASS] Puedes liberar bloques de memoria.'''

    bs = BuddySystem(1024)
    bs.allocate(name='name', size=10)
    out = bs.free(name='name')

    self.assertEqual(out, 'Memoria liberada de forma exitosa (16 bloques).')

  def testFailLiberarInexistente(self):
    '''[FAIL] No puedes liberar bloques de memoria que no existan.'''

    bs = BuddySystem(1024)
    out = bs.free(name='name')

    self.assertEqual(out, 'ERROR: No existe ningun bloque de memoria con el nombre (\'name\').')

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  unittest.main()