import os

from unittest import TestCase

from badimsicore_sniffing_toxml import read_from_pcap, redirect_to_xml, write_to_xml, live_listening, is_valid_extension


class BadimsicoreSniffingTest(TestCase):
    def setUp(self):
        self.exec_path = os.path.dirname(__file__)
        capture = os.path.join(self.exec_path, 'resources/clean/capture.pcap')
        self.input_file = os.path.abspath(capture)
        captured1 = os.path.join(self.exec_path, 'resources/capture1.xml')
        self.captured1 = os.path.abspath(captured1)
        captured2 = os.path.join(self.exec_path, 'resources/capture2.xml')
        self.captured2 = os.path.abspath(captured2)
        self.iface = 'eth0'
        self.net_filter1 = 'gsmtap.chan_type == 1'
        self.net_filter2 = 'gsmtap.chan_type == 2'

    def test_input_not_in_pcap_format(self):
        input_file = 'foo.notpcap'
        ret = is_valid_extension(input_file, '.pcap')
        self.assertFalse(ret)

    def test_output_not_in_xml_format(self):
        output_file = 'foo.notxml'
        ret = is_valid_extension(output_file, '.xml')
        self.assertFalse(ret)

    def test_input_in_pcap_format(self):
        input_file = 'foo.pcap'
        ret = is_valid_extension(input_file, '.pcap')
        self.assertTrue(ret)

    def test_output_in_xml_format(self):
        output_file = 'foo.xml'
        ret = is_valid_extension(output_file, '.xml')
        self.assertTrue(ret)

    def test_read_from_pcap(self):
        print("\ninput : "+self.input_file)
        read_from_pcap(self.input_file, self.iface, self.net_filter1)

    def test_write_to_xml(self):
        # size_captured1 = 2170117
        # size_captured2 = 20325682
        print("\ninput : "+self.input_file)
        print("output : "+self.captured1)
        write_to_xml(self.input_file, self.captured1, self.iface, self.net_filter1)
        # self.assertEqual(size_captured1, os.path.getsize(captured1))
        print("output : "+self.captured2)
        write_to_xml(self.input_file, self.captured2, self.iface, self.net_filter2)
        # self.assertEqual(size_captured2, os.path.getsize(captured2))

    def tearDown(self):
        if os.path.exists(self.captured1):
            os.remove(self.captured1)

        if os.path.exists(self.captured2):
            os.remove(self.captured2)

# TODO : put tests from test_badimsicore_sniffing_xml_parsing.py
