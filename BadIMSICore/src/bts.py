# creating class packet
network_operators = {'01':'Orange', '02':'Orange', '09':'SFR', '10':'SFR', '11':'SFR', '15':'Free', '16':'Free', '20':'Bouygues Telecom', '21':'Bouygues Telecom' }
countries = {'208':'France'}

'''
codes = network_operators.keys()
for code in codes:
    print(network_operators[code])
'''

class BTS:
    """
    Class defining a complete BTS with all informations given from several packets
    The BTS is defined by :
    - LAC
    - Operator
    - Country
    - Cell ID
    - List of ARFCNs
    - Noise Ratio
    """

    def __init__(self, MCC, MNC, LAC, CI, ARFCNs, Ratio):
        """Constructeur de notre classe"""
        self.MCC = countries[MCC]
        self.MNC = network_operators[MNC]
        self.LAC = LAC
        self.CI = CI
        self.ARFCNs = ARFCNs
        self.Ratio = Ratio