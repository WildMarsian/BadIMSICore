#!/usr/bin/env python3.4

 """
    Class defining a complete BTS with all informations given from several packets
    The BTS is defined by :
    - LAC
    - Operator
    - Country
    - Cell ID
    - List of ARFCNs
"""

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team"


class BTS:
    network_operators = {'01': 'Orange', '02': 'Orange', '09': 'SFR', '10': 'SFR', '11': 'SFR', '15': 'Free', '16': 'Free',
                         '20': 'Bouygues', '21': 'Bouygues'}

    countries = {'208': 'France'}

    def __init__(self, MCC, MNC, LAC, CI, ARFCNs=[]):
        self.MCC = MCC
        self.MNC = MNC
        self.shortname = self.network_operators[self.MNC]
        self.LAC = LAC
        self.CI = CI
        self.ARFCNs = sorted(set(ARFCNs))

    def __str__(self):
        s = ""
        for arfcn in self.ARFCNs:
            s += arfcn+", "
        return "BTS: "+self.MNC+" "+self.MCC+" "+self.LAC+" "+self.CI+" -- "+self.shortname+" "+s

    def __eq__(self, other):
        """
            Check if the current bts is equal to the another BTS.
            A BTS is identified by a Cell Identity.
            
            :return : returns True if the two BTS have the same CI,
            otherwise returns False
        """
        return self.CI == other.CI

    def nice_display(self):
        """
            Displays nicely BTS characteristics.
        """
        bts_string = "-> {},{},{},{},".format(self.MNC, self.MCC, self.LAC, self.CI)
        bts_string += str(self.ARFCNs).strip("[]").replace(' ', '')
        return bts_string

    def add_arfcns(self, arfcns):
        """
        fuse a list of arfcn with the one of the bts object
        :param : arfcns: the arfcn to add

        :return : None
        """
        self.ARFCNs.extend(arfcns)
        self.ARFCNs = sorted(set(self.ARFCNs))





