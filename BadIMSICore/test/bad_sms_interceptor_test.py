import unittest

from unittest import TestCase
from bad_sms_interceptor import BadSMSInterceptor


class BadSMSInterceptorTest(TestCase):
    def test_read_no_duplicate(self):
        bsi = BadSMSInterceptor()
        returned_list = bsi.intercept("../src/smqueue.txt")
        size = returned_list.__len__()
        self.assertEquals(5, size)

if __name__ == '__main__':
    unittest.main()
