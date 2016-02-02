import unittest

from src.init_openbts import InitOpenBTS

class init_openbts_test(unittest.TestCase):

    def init_sipauthserve_success_test(self):
        o = InitOpenBTS()
        sortie = o.init_sipauthserve()
        self.assertEquals(True,sortie)

    def init_sipauthserve_fail_test(self):
        o = InitOpenBTS()
        sortie = o.init_sipauthserve()
        self.assertEquals(False,sortie)

if __name__ == '__main__':
    unittest.main()