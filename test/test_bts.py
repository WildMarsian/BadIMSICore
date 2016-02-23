from unittest import TestCase
from bts import BTS

class btsTess(TestCase):

    def setUp(self):
        self.btss = []
        self.btss.append(BTS("208", "01", "LAC1", "CI1", [1,2,4,11,12,13]))
        self.btss.append(BTS("209", "20", "LAC2", "CI2", [567,568,578]))
        self.btss.append(BTS("210", "15", "LAC3", "CI3", [12,13,45,556]))
        self.btss.append(BTS("210", "15", "LAC3", "CI3"))

    def test_input_not_in_pcap_format(self):
        print(self.btss[0].nice_display())
        print(self.btss[1].nice_display())
        print(self.btss[2].nice_display())
        print(self.btss[3].nice_display())

