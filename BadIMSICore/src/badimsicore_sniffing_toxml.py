#!/usr/bin/python3.4

import os
import subprocess
import sys
from optparse import OptionParser

tshark = '/usr/bin/tshark'


def print_error(err):
    print(err)


def live_listening(iface, net_filter):
    pargs = [tshark, '-i', iface]
    pargs.extend(['-T', 'pdml'])

    if net_filter is not None:
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

    if net_filter is not None:
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

            if net_filter is not None:
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


def redirect_to_xml(output_xml_filename, iface, net_filter, duration=10):

    try:
        with open(output_xml_filename, 'w') as output:
            pargs = [tshark, '-i', iface, '-2']
            pargs.extend(['-T', 'pdml'])

            #TODO verifier duration est un entier

            if duration is not None:
                pargs.extend(['-a', 'duration: ' + duration.__str__()])

            if net_filter is not None:
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
    parser = OptionParser(usage='Usage: badimsicore_sniffing_toxml.py -i <input> -o output -d iface -f \'filter\'')
    parser.add_option('-i', '--input', dest='input_filename', help='Input file in PCAP format')
    parser.add_option('-o', '--output', dest='output_filename', help='Output file in XML format')
    parser.add_option('-d', '--device', dest='iface', help='Interface used for listening')
    parser.add_option('-f', '--filter', dest='filter', help='Filter in wireshark style')
    parser.add_option('-t', '--time', dest='time', help='duration of the redirection', default=10)

    (options, args) = parser.parse_args()

    if options.iface is None:
        parser.error('Interface is missing. Please use a valid interface from the system')
    elif options.input_filename is None and options.output_filename is None:
        live_listening(options.iface, options.filter)
    elif options.input_filename is not None and options.output_filename is not None:
        if is_valid_extension(options.input_filename, '.pcap') and is_valid_extension(options.output_filename, '.xml'):
            write_to_xml(options.input_filename, options.output_filename, options.iface, options.filter)
        else:
            parser.error('Invalid formats. Please verify input and output')
    elif options.input_filename is not None and options.output_filename is None:
        if is_valid_extension(options.input_filename, '.pcap'):
            # The user reads from a PCAP file and write to the standard output
            read_from_pcap(options.input_filename, options.iface, options.filter)
        else:
            parser.error('Invalid format for %s' % options.input_filename)
    elif options.input_filename is None and options.output_filename is not None:
        if is_valid_extension(options.output_filename, '.xml'):
            # The user reads from the standard input and write to an XML file
            redirect_to_xml(options.output_filename, options.iface, options.filter, options.time)
        else:
            parser.error('Invalid format for %s' % options.output_filename)
    else:
        print(parser.usage)
        sys.exit(2)

if __name__ == '__main__':
    main()
