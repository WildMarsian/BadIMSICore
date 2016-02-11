import unittest

from unittest import TestCase

from badimsicore_sniffing_gsmband_search import *

class TestRadioBandSearcher(TestCase):

    def test_get_radio_band_by_network_operator_none(self):
        self.o = RadioBandSearcher(None, None, None)
        self.assertEquals(None, self.o.get_radio_band_by_network_operator("Orange"))
        self.assertEquals(None, self.o.get_radio_band_by_network_operator("SFR"))
        self.assertEquals(None, self.o.get_radio_band_by_network_operator("Bouygues Telecom"))

    def test_get_radio_band_by_network_operator_success(self):
        orange_rb = [890.2, 890.4, 890.6, 890.8, 891.0, 891.2]
        sfr_rb = [902.6, 902.8, 903.0]
        bouygues_rb = [880.2, 880.4, 880.6, 883.6]
        self.o = RadioBandSearcher(orange_rb, sfr_rb, bouygues_rb)
        sum_lengths = len(self.o.get_radio_band_by_network_operator("Orange")) + len(self.o.get_radio_band_by_network_operator("Bouygues Telecom")) + len(self.o.get_radio_band_by_network_operator("SFR"))
        self.assertEquals(13, sum_lengths)

    def test_get_radioBandsByOperator(self):
        filename = 'resources/clean/all_gsm_channels_arfcn.csv'
        rb = get_radioBandsByOperator(filename,None)
        self.assertEquals(0, len(rb))

    def test_parse_csv_file(self):
        filename = 'resources/clean/all_gsm_channels_arfcn.csv'
        list_arfcns = []
        radioBands = parse_csv_file(filename, list_arfcns)
        self.assertEquals(0, len(radioBands))

    @unittest.expectedFailure
    def test_get_downlink_from_arfcn_invalid(self):
        filename = 'resources/clean/all_gsm_channels_arfcn.csv'
        list_arfcns = []
        bands = parse_csv_file(filename, list_arfcns)
        downlink_number = get_downlink_from_arfcn(bands, 1234)
        self.fail("this should happen unfortunately")
