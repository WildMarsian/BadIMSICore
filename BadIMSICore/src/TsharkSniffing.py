import os
import subprocess
import time

tshark = '/usr/bin/tshark'


class TShark:
    def __init__(self, pcap_file, xml_file, iface, net_filter):
        '''
        pcap_file:  path on disk to save the pcap file
        xml_file:   path on disk to save the xml file
        iface:      interface which we want to listen
        net_filter: filter
        '''
        self.pcap_file = pcap_file
        self.iface = iface
        self.xml_file = xml_file
        self.proc = None
        self.net_filter = net_filter

        if not os.path.isfile(tshark):
            raise 'Cannot find tshark in ' + tshark

    def start(self):
        '''
        '''
        pargs = [tshark, '-i', self.iface]
        pargs.extend(['-T', 'pdml'])
        if self.net_filter != "":
            pargs.extend(['-R', self.net_filter])

        print(pargs)
        self.proc = subprocess.Popen(pargs)

        return self.proc.communicate()

    def stop(self):
        if self.proc != None and self.proc.poll() == None:
            self.proc.terminate()
            time.sleep(5)

    def write(self):
        '''
        Print statistics and details on packet capture
        '''
        output = open(self.xml_file, 'w')

        proc = subprocess.Popen(
                [
                    tshark, '-i', 'eth0',
                    '-T', 'pdml', '-r',
                    self.pcap_file,
                    '-R', self.net_filter,
                    '-2'
                ]
                ,
                stdout=output
        )
        return proc.communicate()


print("1)Live listening\n2) Read from file")
choice = input()

pcap_input_file = ''
iface = 'eth0'
xml_output_file = ''

if choice == '2':
    print("Input file (PCAP extension) :")
    pcap_input_file = input()
    print("Output file (XML extension) :")
    xml_output_file = input()

print("Interface :")
_iface = input()

print("Filter ('gsmtap.chan_type == 1' or 'gsmtap.chan_type == 2' :")
_net_filter = input()

tshark_proc = TShark(pcap_input_file, xml_output_file, _iface, _net_filter)

if choice == '1':
    tshark_proc.start()
elif choice == '2':
    tshark_proc.write()


tshark_proc.stop()
