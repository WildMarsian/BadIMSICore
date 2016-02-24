#!/usr/bin/env python3.4
import subprocess
import os

from badimsicore_sniffing_gsmband_search import RadioBandSearcher
import badimsicore_sniffing_toxml
import argparse
import badimsicore_sniffing_xml_parsing
import logging

def set_args(parser, bands):
    """
    Set arguments of the command
    :param parser: an argument parser
    :return: None
    """
    group = parser.add_argument_group("listen")
    group.add_argument("-o", "--operator", help="search bts of this operator", default="orange", choices=["orange", "sfr", "bouygues_telecom"])
    group.add_argument("-b", "--band", help="search bts in this band of frequency", default="all", choices=bands)
    group.add_argument("-t", "--scan_time", help="Set the scan time for each frequency", default=2, type=int)
    group.add_argument("-n", "--repeat", help="Set the number of repeat of the scanning cycle", default=1, type=int)
    group.add_argument("-e", "--errors", help="list errors codes", action='store_true')


def scan_frequencies(repeat, scan_time, frequencies):
    """
    Start searching for BTS
    :param repeat: Number of scan cycle
    :param scan_time: Scan time for each ARFCN
    :param frequencies: List of frequency (ARFCN downlink frequencies) to scan
    :return: the exit status of the scan
    """
    opts = ["python2.7", "airprobe_rtlsdr_non_graphical.py"]
    opt_freq = ["-f"]
    frequencies = list(map(lambda freq: str(freq), frequencies))
    opt_freq.extend(frequencies)
    opts.extend(opt_freq)
    opts.extend(['-t', '{: d}'.format(scan_time)])
    opts.extend(['-n', '{: d}'.format(repeat)])
    return subprocess.call(opts)


def toxml(xml_file, duration):
    """
    Start the redirection of all network gsm traffic from lo interface to an XML file
    :param xml_file: XML output file
    :param duration: End of the listening on the interface lo
    :return: The Popen object of the listening process
    """
    return badimsicore_sniffing_toxml.redirect_to_xml(xml_file, "lo", "gsmtap && ! icmp", int(duration + 1))


def parse_xml(xml_file):
    """
    Parse an XML network dump to get a list of BTS
    :param xml_file: The XML network dump file
    :return: a list of BTS cells that have been detected
    """
    return badimsicore_sniffing_xml_parsing.parse_xml_file(xml_file)


def main():
    #parsing arguments
    rds = RadioBandSearcher('../ressources/all_gsm_channels_arfcn.csv')
    bands = rds.get_bands()

    parser = argparse.ArgumentParser()
    set_args(parser, bands)
    args = parser.parse_args()
    if args.errors:
        print("10 : error no frequency to scan")
        print("20 : error scanning for BTS cells")

    #Generating the list of frequencies to scan
    freqs = []
    if args.band == "all":
        for band in bands:
            freqs.extend(rds.get_arfcn(args.operator, band))
    else:
        freqs = rds.get_arfcn(args.operator, args.band)

    if(len(freqs) <= 0):
        print("error no frequency to scan, exiting")
        exit(20)

    #scan duration
    duration = 6 + len(freqs) * args.repeat * args.scan_time

    #start the listening on lo interface
    os.remove("xml_output")
    xml_file = 'xml_output'
    proc = toxml(xml_file, duration)

    #scan frequencies
    if scan_frequencies(args.repeat, args.scan_time, freqs) != 0:
        print("error scanning for BTS cells, exiting")
        exit(10)
    proc.wait()

    #Parse the XML
    btss = parse_xml(xml_file)

    #Print the list of BTS
    for bts in btss:
        print(bts.nice_display())

    exit(0)
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename='sniffing.log', filemod='w', level=logging.INFO)
    logging.info('Logger is lock and loaded')
    main()
