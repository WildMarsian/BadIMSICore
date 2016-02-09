import unittest
import os

from unittest import TestCase
from badimsicore_sms_interceptor import BadSMSInterceptor


class BadSMSInterceptorTest(TestCase):

    @unittest.skipIf(os.path.exists("../src/smqueue.txt.offset"), "Offset exists, skipping test")
    def test_read_no_duplicate(self):
        bsi = BadSMSInterceptor()
        returned_list = bsi.intercept("../src/smqueue.txt")
        size = list(returned_list).__len__()
        self.assertEquals(5, size)
        pass

    @unittest.skipUnless(os.path.exists("../src/smqueue.txt.offset"), "Offset exists, skipping test")
    def test_no_entries_after_first_read(self):
        bsi = BadSMSInterceptor()
        bsi.intercept("../src/smqueue.txt")
        returned_list = bsi.intercept("../src/smqueue.txt")
        size = returned_list.__len__()
        self.assertEqual(0, size)
        pass

if __name__ == '__main__':
    unittest.main()
