import csv


class ARFCN:

    def __init__(self, arfcn, downlink, uplink, band):
        self.arfcn = arfcn
        self.downlink = downlink
        self.uplink = uplink
        self.band = band

    def get_operator(self):
        return ARFCN.get_operator_from_arfcn(self.arfcn)

    def __str__(self):
        return '({self.arfcn}, {self.downlink}, {self.uplink}, {self.band})'.format(self=self)

    def __lt__(self, other):
        return self.arfcn < other.arfcn

    def __gt__(self, other):
        return self.arfcn > other.arfcn


    @staticmethod
    def get_operator_from_arfcn(arfcn):
        """
        Give the network operator linked to an arfcn number
        :return the network operator (String)
        :param arfcn, design the arfcn number (int)
        """
        if(1 <= arfcn and arfcn <= 62) or (527 <= arfcn and arfcn <= 645):
            return "orange"
        elif(63 <= arfcn and arfcn <= 124) or (512 <= arfcn and arfcn <= 525) or (647 <= arfcn and arfcn <= 751):
            return "sfr"
        elif(753 <= arfcn and arfcn <= 885) or (975 <= arfcn and arfcn <= 1023):
            return "bouygues_telecom"
        else:
            return "None"


class RadioBandSearcher:

    def __init__(self, filename):
        self.arfcn_dict = csv_arfcn_dict_reader(filename)

    def get_arfcn(self, operator, band):
        results = self.arfcn_dict.get(band).get(operator)
        if results is None:
            return []
        return list(map(lambda arfcn_object: arfcn_object.downlink*1000000, self.arfcn_dict.get(band).get(operator).values()))

    def get_bands(self):
        return self.arfcn_dict.keys()

def csv_arfcn_dict_reader(filename):
    """
    Read a CSV file using csv.DictReader and return it into a dictionary that contains {ARFCN number : informations}
    :param filename the csv file to read
    :return: a dictionary containing ARFCN object
    """
    arfcn_dict = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for line in reader:
            band_value = line['name']
            arfcn_value = int(line['arfcn'])
            uplink_value = float(line['uplink'])
            downlink_value = float(line['downlink'])

            arfcn_dict_band = arfcn_dict.get(band_value)
            if arfcn_dict_band is None:
                arfcn_dict_band = {}
                arfcn_dict[band_value] = arfcn_dict_band

            afrcn_dict_op = arfcn_dict_band.get(ARFCN.get_operator_from_arfcn(arfcn_value))
            if afrcn_dict_op is None:
                afrcn_dict_op = {}
                arfcn_dict_band[ARFCN.get_operator_from_arfcn(arfcn_value)] = afrcn_dict_op

            afrcn_dict_op[arfcn_value] = ARFCN(arfcn_value, downlink_value, uplink_value, band_value)

        return arfcn_dict

def print_error(err):
    """
    :param err: the error String message
    :return: void
    """
    print(err)

if __name__ == "__main__":

    rbs = RadioBandSearcher('resources/all_gsm_channels_arfcn.csv')
    print(rbs.arfcn_dict)
    print("Searching radio bands by network operator: ")
    print("Orange bands: ", sorted(rbs.get_arfcn("orange", "GSM-900")))
    print("SFR bands: ", sorted(rbs.get_arfcn("sfr", "GSM-900")))
    print("Bouygues Telecom bands: ", sorted(rbs.get_arfcn("bouygues_telecom", "EGSM-900")))

