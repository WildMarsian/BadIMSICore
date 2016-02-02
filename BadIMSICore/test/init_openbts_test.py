import unittest

from src import init_openbts

class init_openbts_test(unittest.TestCase):

    def init_sipauthserve_success_test(self):
        sortie = init_openbts.init_sipauthserve()
        self.assertEquals(True,sortie)

    def init_sipauthserve_fail_test(self):
        sortie = init_openbts.init_sipauthserve()
        self.assertEquals(False,sortie)

if __name__ == '__main__':
    unittest.main()