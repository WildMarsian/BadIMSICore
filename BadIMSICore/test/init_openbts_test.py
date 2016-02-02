import unittest

from unittest import TestCase

from init_openbts import InitOpenBTS


class init_openbts_test(TestCase):

    def test_init_sipauthserve_failed(self):
        o = InitOpenBTS()
        self.assertEquals(False,o.init_sipauthserve())

if __name__ == '__main__':
    unittest.main()