
from unittest import TestCase
import os

from badimsicore_sniffing_gsmband_search import *


class TestRadioBandSearcher(TestCase):

    def setUp(self):
        self.exec_path = os.path.dirname(__file__)
        capture = os.path.join(self.exec_path, 'ressources/clean/all_gsm_channels_arfcn.csv')
        self.arfcn_csv = os.path.abspath(capture)

        self.orange_gsm_900 = [890.2, 890.4, 890.6, 890.8, 891.0, 891.2, 891.4, 891.6, 891.8, 892.0, 892.2, 892.4, 892.6, 892.8, 893.0, 893.2, 893.4, 893.6, 893.8, 894.0, 894.2, 894.4, 894.6, 894.8, 895.0, 895.2, 895.4, 895.6, 895.8, 896.0, 896.2, 896.4, 896.6, 896.8, 897.0, 897.2, 897.4, 897.6, 897.8, 898.0, 898.2, 898.4, 898.6, 898.8, 899.0, 899.2, 899.4, 899.6, 899.8, 900.0, 900.2, 900.4, 900.6, 900.8, 901.0, 901.2, 901.4, 901.6, 901.8, 902.0, 902.2, 902.4]
        self.sfr_gsm_900 = [902.6, 902.8, 903.0, 903.2, 903.4, 903.6, 903.8, 904.0, 904.2, 904.4, 904.6, 904.8, 905.0, 905.2, 905.4, 905.6, 905.8, 906.0, 906.2, 906.4, 906.6, 906.8, 907.0, 907.2, 907.4, 907.6, 907.8, 908.0, 908.2, 908.4, 908.6, 908.8, 909.0, 909.2, 909.4, 909.6, 909.8, 910.0, 910.2, 910.4, 910.6, 910.8, 911.0, 911.2, 911.4, 911.6, 911.8, 912.0, 912.2, 912.4, 912.6, 912.8, 913.0, 913.2, 913.4, 913.6, 913.8, 914.0, 914.2, 914.4, 914.6, 914.8]
        self.bouygues_egsm_900 = [880.2, 880.4, 880.6, 880.8, 881.0, 881.2, 881.4, 881.6, 881.8, 882.0, 882.2, 882.4, 882.6, 882.8, 883.0, 883.2, 883.4, 883.6, 883.8, 884.0, 884.2, 884.4, 884.6, 884.8, 885.0, 885.2, 885.4, 885.6, 885.8, 886.0, 886.2, 886.4, 886.6, 886.8, 887.0, 887.2, 887.4, 887.6, 887.8, 888.0, 888.2, 888.4, 888.6, 888.8, 889.0, 889.2, 889.4, 889.6, 889.8]

    def test_get_radio_band_by_network_operator_orange(self):
        rbs = RadioBandSearcher(self.arfcn_csv)
        self.assertEquals(rbs.get_arfcn("orange", "GSM-900"), self.orange_gsm_900)

    def test_get_radio_band_by_network_operator_sfr(self):
        rbs = RadioBandSearcher(self.arfcn_csv)
        self.assertEquals(rbs.get_arfcn("sfr", "GSM-900"), self.sfr_gsm_900)

    def test_get_radio_band_by_network_operator_bouy(self):
        rbs = RadioBandSearcher(self.arfcn_csv)
        self.assertEquals(rbs.get_arfcn("bouygues_telecom", "EGSM-900"), self.bouygues_egsm_900)

    def test_get_radio_band_by_network_operator_bouy_none(self):
        rbs = RadioBandSearcher(self.arfcn_csv)
        self.assertEquals(rbs.get_arfcn("bouygues_telecom", "GSM-900"), [])
