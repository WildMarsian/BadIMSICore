import unittest
import os

from unittest import TestCase
from badimsicore_sms_interceptor import BadSMSInterceptor

exec_path = os.path.dirname(__file__)
filename = os.path.join(exec_path, 'resources/clean/smqueue.txt')
offset_file = os.path.abspath(filename)


class BadSMSInterceptorTest(TestCase):
    def setUp(self):
        self.bsi = BadSMSInterceptor()
        self.exec_path = os.path.dirname(__file__)
        filename = os.path.join(self.exec_path, 'resources/clean/smqueue.txt')
        self.input_file = os.path.abspath(filename)

    @unittest.skipIf(os.path.exists(offset_file), "Offset exists, skipping test")
    def test_read_no_duplicate(self):
        #bsi = BadSMSInterceptor()
        returned_list = self.bsi.intercept(self.input_file)
        size = list(returned_list).__len__()
        self.assertEquals(5, size)
        pass

    @unittest.skipUnless(os.path.exists(offset_file), "Offset exists, skipping test")
    def test_no_entries_after_first_read(self):
        #bsi = BadSMSInterceptor()
        self.bsi.intercept(self.input_file)
        returned_list = self.bsi.intercept(self.input_file)
        size = returned_list.__len__()
        self.assertEqual(0, size)
        pass

if __name__ == '__main__':
    unittest.main()
