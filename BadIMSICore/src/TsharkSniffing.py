import os
import subprocess

tshark = '/usr/bin/tshark'


class TsharkSniffing:
    def __init__(self):
        if not os.path.isfile(tshark):
            raise 'Cannot find tshark in ' + tshark

    def live_listening(self, iface, net_filter):
        if iface == '':
            raise 'Interface not defined'

        pargs = [tshark, '-i', iface]
        pargs.extend(['-T', 'pdml'])

        if net_filter != "":
            pargs.extend(['-R', net_filter])

        print(pargs)
        proc = subprocess.Popen(pargs)

        return proc.communicate()

    def read_from_pcap(self, input_pcap_filename, iface, net_filter):
        if iface == '':
            raise 'Interface not defined'
        if not os.path.isfile(input_pcap_filename):
            raise 'Input PCAP file not found'

        pargs = [tshark, '-i', iface]
        pargs.extend(['-r', input_pcap_filename])
        pargs.extend(['-T', 'pdml'])

        if net_filter != '':
            pargs.extend(['-R', net_filter])

        proc = subprocess.Popen(pargs)

        return proc.communicate()

    def write_to_xml(self, input_pcap_filename, output_xml_filename, iface, net_filter):
        if iface == '':
            raise 'Interface not defined'
        if not os.path.isfile(input_pcap_filename):
            raise 'Input PCAP file not found'
        output = open(output_xml_filename, 'w')

        pargs = [tshark, '-i', iface, '-2']
        pargs.extend(['-r', input_pcap_filename])
        pargs.extend(['-T', 'pdml'])

        if net_filter != '':
            pargs.extend(['-R', net_filter])

        proc = subprocess.Popen(pargs, stdout=output)

        return proc.communicate()


tshark_proc = TsharkSniffing()

print("Interface :")
_iface = input()

print("Filter ('gsmtap.chan_type == 1' or 'gsmtap.chan_type == 2' :")
_net_filter = input()

print("1)Live listening\n2) Read from file and show into the standard output" +
      "\n3)Read from file and write into a another file :")
choice = input()

if choice == '1':
    tshark_proc.live_listening(_iface, _net_filter)

elif choice == '2':
    print("PCAP file name :")
    input_pcap_file_name = input()
    tshark_proc.read_from_pcap(input_pcap_file_name, _iface, _net_filter)

elif choice == '3':
    print("PCAP file name :")
    input_pcap_filename = input()
    print("XML file name :")
    output_xml_filename = input()
    tshark_proc.write_to_xml(input_pcap_filename, output_xml_filename, _iface, _net_filter)
