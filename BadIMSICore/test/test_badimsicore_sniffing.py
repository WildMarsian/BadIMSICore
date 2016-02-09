import os

from unittest import TestCase

from badimsicore_sniffing import read_from_pcap, redirect_to_xml, write_to_xml, live_listening, is_valid_extension


class BadimsicoreSniffingTest(TestCase):

    def test_input_not_in_pcap_format(self):
        input_file = 'foo.notpcap'
        ret = is_valid_extension(input_file, '.pcap')
        self.assertFalse(ret)

    def test_output_not_in_xml_format(self):
        output_file = 'foo.notxml'
        ret = is_valid_extension(output_file, '.xml')
        self.assertFalse(ret)

    def test_read_from_pcap(self):
        exec_path = os.path.dirname(__file__)
        capture = os.path.join(exec_path, 'resources/clean/capture.pcap')
        input_file = os.path.abspath(capture)
        print("\ninput : "+input_file)
        read_from_pcap(input_file, 'eth0', 'gsmtap.chan_type == 1')

    def test_write_to_xml(self):
        exec_path = os.path.dirname(__file__)
        capture = os.path.join(exec_path, 'resources/clean/capture.pcap')
        captured1 = os.path.join(exec_path, 'resources/capture1.xml')
        captured2 = os.path.join(exec_path, 'resources/capture2.xml')
        input_file = os.path.abspath(capture)
        output_file = os.path.abspath(captured1)
        size_captured1 = 2170117
        size_capture2 = 20325682
        print("\ninput : "+input_file)
        print("output : "+output_file)
        write_to_xml(input_file, output_file, 'eth0', 'gsmtap.chan_type == 1')
        self.assertEqual(size_captured1, os.path.getsize(captured1))
        output_file = os.path.abspath(captured2)
        write_to_xml(input_file, output_file, 'eth0', 'gsmtap.chan_type == 2')
        self.assertEqual(size_capture2, os.path.getsize(captured2))

