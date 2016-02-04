# creating class packet
class BTS:
    """
    Class defining a complete BTS with all informations given from several packets
    The BTS is defined by :
    - LAC
    - Operator
    - Cell ID
    - List of ARFCNs
    - Noise Ratio
    """

    def __init__(self, MCC, MNC, LAC, CI, ARFCNs, Ratio):
        """Constructeur de notre classe"""
        self.MCC = MCC
        self.MNC = MNC
        self.LAC = LAC
        self.CI = CI
        self.ARFCNs = ARFCNs
        self.Ratio = Ratio