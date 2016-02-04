# listing all the networks code
network_operators = {'01':'Orange', '02':'Orange', '09':'SFR', '10':'SFR', '11':'SFR', '15':'Free', '16':'Free', '20':'Bouygues Telecom', '21':'Bouygues Telecom' }
countries = {'208':'France'}

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
        self.LAC = LAC
        self.CI = CI
        self.ARFCNs = ARFCNs