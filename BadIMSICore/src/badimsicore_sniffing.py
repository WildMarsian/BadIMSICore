#!/usr/bin/python3.4

import os
import subprocess
import getopt
import sys

tshark = '/usr/bin/tshark'


def usage():
    print("Usage: badimsicore_sniffing.py -i <input.pcap> -o <output.xml> -d iface -f 'filter'")


def print_error(err):
    print(err)


def live_listening(iface, net_filter):
    pargs = [tshark, '-i', iface]
    pargs.extend(['-T', 'pdml'])

    if len(net_filter) > 0:
        pargs.extend(['-R', net_filter])

    # print(pargs)
    proc = subprocess.Popen(pargs)

    return proc.communicate()


"""
Reads a PCAP file
"""


def read_from_pcap(input_pcap_filename, iface, net_filter):
    if not os.path.isfile(input_pcap_filename):
        raise FileNotFoundError('Input PCAP file not found')

    pargs = [tshark, '-i', iface, '-2']
    pargs.extend(['-r', input_pcap_filename])
    pargs.extend(['-T', 'pdml'])

    if len(net_filter) > 0:
        pargs.extend(['-R', net_filter])

    # We don't need the output
    proc = subprocess.Popen(pargs, stdout=subprocess.PIPE)

    return proc.communicate()


"""
TODO : debug function
"""
"""
def write_to_pcap(output_pcap_filename, iface, net_filter):
    # TODO : test extension
    pargs = [tshark, '-i', iface, '-2']
    pargs.extend(['-w', output_pcap_filename])
    pargs.extend(['-T', 'pdml'])

    if net_filter != '':
        pargs.extend(['-R', net_filter])

    proc = subprocess.Popen(pargs)

    return proc.communicate()
"""

"""
 Write the traffic from an PCAP file to an XML file
"""


def write_to_xml(input_pcap_filename, output_xml_filename, iface, net_filter):
    try:
        with open(output_xml_filename, 'w') as output:

            """Here we don't need to open the input file, because this action
            is realized by tshark
            """
            if not os.path.exists(input_pcap_filename) and not os.path.isfile(input_pcap_filename):
                raise FileNotFoundError('Input PCAP file not found')

            pargs = [tshark, '-i', iface, '-2']
            pargs.extend(['-r', input_pcap_filename])
            pargs.extend(['-T', 'pdml'])

            if len(net_filter) > 0:
                pargs.extend(['-R', net_filter])

            proc = subprocess.Popen(pargs, stdout=output)
            return proc.communicate()

    # Problem while opening the output file
    except IOError as err:
        print_error(err)
        sys.exit(2)


"""
Write the trafic from the standard input to an XML file
"""


def redirect_to_xml(output_xml_filename, iface, net_filter):
    # TODO : test extension

    try:
        with open(output_xml_filename, 'w') as output:
            pargs = [tshark, '-i', iface, '-2']
            pargs.extend(['-T', 'pdml'])

            if len(net_filter) > 0:
                pargs.extend(['-R', net_filter])

            proc = subprocess.Popen(pargs, stdout=output)
            return proc.communicate()

    # Problem while opening the output file
    except IOError as err:
        print_error(err)
        sys.exit(2)


"""
Tests if the filename is to ext format.
    :param   filename the filename to check
    :returns    True if ext is valid
    :returns    False otherwise
"""


def is_valid_extension(filename, ext):
    filename, extension = os.path.splitext(filename)
    return extension == ext


def main():
    input_pcap_filename = ''
    output_filename = ''
    iface = ''
    net_filter = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:w:d:f:",
                                   ["help", "input=", "output=", "write=", "dev=", "filter="])
    except getopt.GetoptError as err:
        print_error(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-i", "--input"):
            input_pcap_filename = arg
            print(input_pcap_filename)
        elif opt in ("-o", "--output"):
            output_filename = arg
            print(output_filename)
        elif opt in ("-w", "--write"):
            output_filename = arg
            print(output_filename)
        elif opt in ("-d", "--dev"):
            iface = arg
            print(iface)
        elif opt in ("-f", "--filter"):
            net_filter = arg
            print(net_filter)
        else:
            assert False, "Unhandled exception"

    if len(iface) > 0:
        # Six characters minimum for the input file
        if len(input_pcap_filename) > 5:
            if not is_valid_extension(input_pcap_filename, '.pcap'):
                usage()
                sys.exit(2)

        # Five characters minimum for the input file
        if len(output_filename) > 4:
            if not is_valid_extension(output_filename, '.xml'):
                usage()
                sys.exit(2)

        # The user reads from a PCAP file and write to an XML file
        if len(input_pcap_filename) > 5 and len(output_filename) > 4:
            write_to_xml(input_pcap_filename, output_filename, iface, net_filter)
        # The user reads from a PCAP file and write to the standard output
        elif len(input_pcap_filename) > 5 and len(output_filename) == 0:
            read_from_pcap(input_pcap_filename,iface,net_filter)
        # The user reads from the standard input and write to an XML file
        elif len(input_pcap_filename) == 0 and len(output_filename) > 4:
            redirect_to_xml(output_filename, iface, net_filter)
        else:
            live_listening(iface, net_filter)
    else:
        usage()
        sys.exit(2)

if __name__ == '__main__':
    main()
