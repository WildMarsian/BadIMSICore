#!/usr/bin/env python3.4
import subprocess
import argparse
from badimsicore_sniffing_gsmband_search import RadioBandSearcher


def set_args(parser):
    group = parser.add_argument_group("listen")
    group.add_argument("-o", "--operator", help="search bts of this operator", default="orange", choices=["orange", "sfr", "bouygues_telecom"])
    group.add_argument("-b", "--band", help="search bts in this band of frequency", default="all")
    group.add_argument("-t", "--scan_time", help="Set the scan time for each frequency", default=2, type=int)
    group.add_argument("-n", "--repeat", help="Set the number of repeat of the scanning cycle", default=1, type=int)


def main():
    parser = argparse.ArgumentParser()
    set_args(parser)
    args = parser.parse_args()
    rds = RadioBandSearcher('../ressources/all_gsm_channels_arfcn.csv')
    bands = rds.get_bands()
    freqs = []
    if args.band == "all":
        for band in bands:
            freqs.extend(rds.get_arfcn(args.operator, band))
    else:
        freqs = rds.get_arfcn(args.operator, args.band)

    duration = 6 + len(freqs) * args.repeat * args.scan_time

    opts = ['python2.7', 'airprobe_rtlsdr_non_graphical.py',
            '-f', '937800000',
            '-t', '{: d}'.format(args.scan_time),
            '-n', '{: d}'.format(args.repeat)]
    subprocess.call(opts)

if __name__ == '__main__':
    main()
