import unittest

from unittest import TestCase
from init_openbts import InitOpenBTS


class InitOpenBTSTest(TestCase):
    def test_init_sipauthserve_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.init_sipauthserve())

    def test_stop_sipauthserve_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.stop_sipauthserve())

    def test_init_smqueue_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.init_smqueue())

    def test_stop_smqueue_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.stop_smqueue())

    def test_init_transceiver_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.init_transceiver())

    def test_init_openbts_fail(self):
        o = InitOpenBTS()
        self.assertEquals(False, o.init_openbts())

if __name__ == '__main__':
    unittest.main()
