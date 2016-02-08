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
        input_file = 'resources/clean/capture.pcap'
        read_from_pcap(input_file, 'eth0', 'gsmtap.chan_type == 1')

    def test_write_to_xml(self):
        input_file = 'resources/clean/capture.pcap'
        output_file = 'resources/capture.xml'
        write_to_xml(input_file, output_file, 'eth0', 'gsmtap.chan_type == 1')

