import csv
import sys

# ----------------------------------------------------------------- #


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
        tuple = (arfcn_number,line['downlink'],line['uplink'])
        tuples[arfcn_number] = tuple
    return tuples

# ----------------------------------------------------------------- #

def get_downlink_from_arfcn(tuples, arfcn):
    """
    :param tuples: a dictionnary
    :param arfcn: the arfcn number
    :return: the downlink number of an arfcn
    """

    tuple_arfcn = tuples[arfcn]
    return tuple_arfcn[1]

def print_error(err):
    """
    :param err: the error String message
    :return: void
    """
    print(err)

def parse_csv_file(filename):
    try:
        with open(filename) as f_obj:
            tuples = csv_dict_reader(f_obj)
        for index in sorted(tuples.keys()):
            print(index, tuples[index])
            print("Downlink", get_downlink_from_arfcn(tuples,index))
            # Problem while opening the output file

    except IOError as err:
        print_error(err)
        sys.exit(2)

# ----------------------------------------------------------------- #
if __name__ == "__main__":
    filename ='../ressources/all_gsm_channels_arfcn.csv'
    parse_csv_file(filename)