import unittest

from unittest import TestCase
from badimsicore_sniffing_xml_parsing import is_valid_extension
from badimsicore_sniffing_xml_parsing import parse_xml_file


class XMLParsingTest(TestCase):
    def test_input_not_in_xml_format(self):
        self.assertEquals(False, is_valid_extension('myfile.txt', '.xml'))


if __name__ == '__main__':
    unittest.main()

