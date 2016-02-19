# listing all the networks code
network_operators = {'01': 'Orange', '02': 'Orange', '09': 'SFR', '10': 'SFR', '11': 'SFR', '15': 'Free', '16': 'Free',
                     '20': 'Bouygues', '21': 'Bouygues'}
countries = {'208': 'France'}


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
    def __init__(self, MCC, MNC, LAC, CI, ARFCNs):
        self.MCC = MCC
        self.MNC = MNC
        self.shortname = network_operators[self.MNC]
        self.LAC = LAC
        self.CI = CI
        self.ARFCNs = sorted(ARFCNs)

    def __str__(self):
        s = ""
        for arfcn in self.ARFCNs:
            s += arfcn+", "
        return "BTS: "+self.MNC+" "+self.MCC+" "+self.LAC+" "+self.CI+" -- "+self.shortname+" "+s

    def __eq__(self, other):
        return self.MCC == other.MCC and self.MNC == other.MNC and self.LAC == other.LAC and self.ARFCNs == other.ARFCNs and self.CI == other.CI


