#!/usr/bin/python3.4

import unittest

from unittest import TestCase
from badimsicore_openbts_init import InitOpenBTS


class InitOpenBTSTest(TestCase):
    def setUp(self):
        self.o = InitOpenBTS()

    def test_init_sipauthserve_fail(self):
        self.assertEquals(False, self.o.init_sipauthserve())

    def test_stop_sipauthserve_fail(self):
        self.assertEquals(False, self.o.stop_sipauthserve())

    def test_init_smqueue_fail(self):
        self.assertEquals(False, self.o.init_smqueue())

    def test_stop_smqueue_fail(self):
        self.assertEquals(False, self.o.stop_smqueue())

    def test_init_transceiver_fail(self):
        self.assertEquals(False, self.o.init_transceiver())

    def test_init_openbts_fail(self):
        self.assertEquals(False, self.o.init_openbts())

if __name__ == '__main__':
    unittest.main()
