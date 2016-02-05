import unittest

from unittest import TestCase
from badimsicore_sniffing_xml_parsing import is_valid_extension
from badimsicore_sniffing_xml_parsing import parse_xml_file


class XMLParsingTest(TestCase):
    def test_file_format_failed(self):
        return self.assertEquals(False, is_valid_extension('myfile.txt', '.xml'))


if __name__ == '__main__':
    unittest.main()

