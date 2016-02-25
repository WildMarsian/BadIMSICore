class BTS:
    """
    Class defining a complete BTS with all informations given from several packets
    The BTS is defined by :
    - LAC
    - Operator
    - Country
    - Cell ID
    - List of ARFCNs
    """

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
        return self.CI == other.CI

    def nice_display(self):
        bts_string = "-> {},{},{},{},".format(self.MNC, self.MCC, self.LAC, self.CI)
        bts_string += str(self.ARFCNs).strip("[]").replace(' ', '')
        return bts_string

    def add_arfcns(self, arfcns):
        self.ARFCNs.extend(arfcns)
        self.ARFCNs = sorted(set(self.ARFCNs))





