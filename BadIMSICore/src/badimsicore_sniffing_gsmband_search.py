import csv
import sys


class RadioBandSearcher:
    def __init__(self, orange_rb, sfr_rb, bouygues_rb):
        self.orange_rb = orange_rb
        self.sfr_rb = sfr_rb
        self.bouygues_rb = bouygues_rb

    def get_radio_band_by_network_operator(self, operator):
        if(operator == "Orange"):
            return self.orange_rb
        if(operator == "SFR"):
            return self.sfr_rb
        if(operator == "Bouygues Telecom"):
            return self.bouygues_rb

# --------------------------------------------- -------------------- #

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader and return it into a dictionary that contains {ARFCN number : informations}
    :param file_obj: the csv file to read
    :return: a dictionary
    """
    tuples = {}
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        arfcn_number = int(line['arfcn'])
        tuple = (arfcn_number,float(line['downlink']),float(line['uplink']))
        tuples[arfcn_number] = tuple
    return tuples
def get_network_operator_by_arfcn(arfcn):
    """
    Give the network operator linked to an arfcn number
    :param arfcn: the arfcn number.
    :return: the network operator (String)
    """
    if(1<=arfcn and arfcn<=62) or (527<=arfcn and arfcn<=645):
        return "Orange"
    if(63<=arfcn and arfcn<=124) or (512<=arfcn and arfcn<=525) or (647<=arfcn and arfcn<=751):
        return "SFR"
    if(753<=arfcn and arfcn<=885) or (975<=arfcn and arfcn<=1023):
        return "Bouygues Telecom"

def print_error(err):
    """
    :param err: the error String message
    :return: void
    """
    print(err)

def get_radioBandsByOperator(filename, operator):
    """
    Gives a list of all GSM bands linked to the network operator given in parameter.
    :param filename: the csv file
    :param operator: the network operator (String)
    :return: a list that contains the network operator bands
    """
    try:
        radioBands = []
        tuple = ()
        if(operator == None):
            return radioBands
        with open(filename) as f_obj:
            tuples = csv_dict_reader(f_obj)

        for element in sorted(tuples.keys()):
            if(get_network_operator_by_arfcn(element) == operator):
                radioBands.append(get_downlink_from_arfcn(tuples,element))
        return radioBands

    except IOError as err:
        print_error(err)
        sys.exit(2)

def parse_csv_file(filename, list_arfcns):
    try:
        radioBands = []
        tuple = ()
        if(len(list_arfcns) == 0):
            return radioBands
        with open(filename) as f_obj:
            tuples = csv_dict_reader(f_obj)
        for arfcn in list_arfcns:
            tuple = (get_network_operator_by_arfcn(arfcn), get_downlink_from_arfcn(tuples,arfcn))
            radioBands.append(tuple)
        return radioBands
    except IOError as err:
        print_error(err)
        sys.exit(2)

def get_downlink_from_arfcn(tuples, arfcn):
    """
    Getting the downlink frequency from an arfcn number
    :param tuples: a dictionnary
    :param arfcn: the arfcn number
    :return: the downlink number of an arfcn
    """
    if(arfcn > len(tuples)):
        return None
    tuple_arfcn = tuples[arfcn]
    if len(tuple_arfcn) == 0:
        return None
    return tuple_arfcn[1]


# ----------------------------------------------------------------- #
if __name__ == "__main__":
    filename ='../ressources/all_gsm_channels_arfcn.csv'

    list_arfcns = [1010, 779, 791, 794, 875, 876, 878, 883, 982]
    bands = parse_csv_file(filename, list_arfcns)

    print("With a list of ARFCN: ")
    print("ARFCN: ", list_arfcns)
    print("BANDS: ", bands)
    print("----------------------")

    orange_radioBands = get_radioBandsByOperator(filename,"Orange")
    sfr_radioBands = get_radioBandsByOperator(filename, "SFR")
    bouygues_radioBands = get_radioBandsByOperator(filename, "Bouygues Telecom")

    rbs = RadioBandSearcher(orange_radioBands,sfr_radioBands, bouygues_radioBands)
    print("Searching radio bands by network operator: ")
    print("Orange bands: ",sorted(rbs.get_radio_band_by_network_operator("Orange")))
    print("SFR bands: ",sorted(rbs.get_radio_band_by_network_operator("SFR")))
    print("Bouygues Telecom bands: ",sorted(rbs.get_radio_band_by_network_operator("Bouygues Telecom")))
