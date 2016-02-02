import unittest

from src.init_openbts import init_sipauthserve
class init_openbts_test(unittest.TestCase):
    def init_sipauthserve_success_test(self):
        sortie = init_sipauthserve()
        print(sortie)
        self.assertEquals(True,sortie)
    def init_sipauthserve_fail_test(self):
        sortie = init_sipauthserve()
        print(sortie)
        self.assertEquals(False,sortie)
if __name__ == '__main__':
    unittest.main()