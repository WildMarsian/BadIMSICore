#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Airprobe Rtlsdr
# Generated: Wed Fev 10 17:27:21 2016
##################################################

from gnuradio import blocks
from gnuradio import gr
from math import pi
import grgsm
import osmosdr
import pmt
import sys
import time
import logging
from threading import Thread
import argparse

class airprobe_rtlsdr(gr.top_block):

    def __init__(self, fc, gain, ppm, samp_rate, shiftoff):
        # Initiating the herited top_block class of the gnuradio project
        gr.top_block.__init__(self, "Airprobe Rtlsdr")

        # Settting parameters of the class
        self.fc = fc
        self.gain = gain
        self.ppm = ppm
        self.samp_rate = samp_rate
        self.shiftoff = shiftoff

        # Initialisation of the rtlsdr module to communicate with the device
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.fc-self.shiftoff, 0)
        self.rtlsdr_source_0.set_freq_corr(self.ppm, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(self.gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(250e3+abs(self.shiftoff), 0)

        self.gsm_sdcch8_demapper_0 = grgsm.universal_ctrl_chans_demapper(1, ([0,4,8,12,16,20,24,28,32,36,40,44]), ([8,8,8,8,8,8,8,8,136,136,136,136]))
        self.gsm_receiver_0 = grgsm.receiver(4, ([0]), ([]))
        # Setting block to display received packets in the terminal
        self.gsm_message_printer_1 = grgsm.message_printer(pmt.intern(""), False)
        # Setting gr-gsm parameters to listen the network
        self.gsm_input_0 = grgsm.gsm_input(
            ppm=self.ppm,
            osr=4,
            fc=self.fc,
            samp_rate_in=self.samp_rate,
        )

        # Getting the GSM packet decoder
        self.gsm_decryption_0 = grgsm.decryption(([]), 1)
        # Create the control channel decoder to receive GSM packets
        self.gsm_control_channels_decoder_0_0 = grgsm.control_channels_decoder()
        # Create a duplicate control channel to display in the terminal
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        # TODO comment
        self.gsm_clock_offset_control_0 = grgsm.clock_offset_control(self.fc-self.shiftoff)
        # Create the BCCH and CCCH channel "parser?"
        self.gsm_bcch_ccch_demapper_0 = grgsm.universal_ctrl_chans_demapper(0, ([2,6,12,16,22,26,32,36,42,46]), ([1,2,2,2,2,2,2,2,2,2]))
        # Creating a client socket connected to the loopback interface
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "4729", 10000)
        # Creating a server socket to use GSM packets without Wireshark or other traffic analyser
        #self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", "127.0.0.1", "4729", 10000)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-2*pi*self.shiftoff/self.samp_rate)

        # Sending received traffic from the device to the BCCH and CCCH channel mapper
        self.msg_connect((self.gsm_receiver_0, 'C0'), (self.gsm_bcch_ccch_demapper_0, 'bursts'))
        # Sending received traffic from the device to the Clock Offset controler
        self.msg_connect((self.gsm_receiver_0, 'measurements'), (self.gsm_clock_offset_control_0, 'measurements'))
        # Sending received traffic from the device to the SDCCH channel mapper
        self.msg_connect((self.gsm_receiver_0, 'C0'), (self.gsm_sdcch8_demapper_0, 'bursts'))
        # TODO comment
        self.msg_connect((self.gsm_clock_offset_control_0, 'ppm'), (self.gsm_input_0, 'ppm_in'))

        # Sending SDCCH channel packets decoded to the GSM decrypter
        self.msg_connect((self.gsm_sdcch8_demapper_0, 'bursts'), (self.gsm_decryption_0, 'bursts'))
        # Sending decrypted GSM packets to the channel decoder
        self.msg_connect((self.gsm_decryption_0, 'bursts'), (self.gsm_control_channels_decoder_0, 'bursts'))
        # Connecting the BCCH and CCCH channel mapper to the channel decoder
        self.msg_connect((self.gsm_bcch_ccch_demapper_0, 'bursts'), (self.gsm_control_channels_decoder_0, 'bursts'))
        # Sending readable GSM packets to the client socket
        self.msg_connect((self.gsm_control_channels_decoder_0, 'msgs'), (self.blocks_socket_pdu_0, 'pdus'))

        self.connect((self.rtlsdr_source_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.gsm_input_0, 0))
        self.connect((self.gsm_input_0, 0), (self.gsm_receiver_0, 0))        

    # Get the sample rate value
    def get_samp_rate(self):
        return self.samp_rate

    # Set the sample rate value
    def set_samp_rate(self, samp_rate):
        logging.info('Changing the sample rate from %s to  %s', self.samp_rate, samp_rate)
        self.samp_rate = samp_rate
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)
        self.gsm_input_0.set_samp_rate_in(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    # Get the current shiftoff value
    def get_shiftoff(self):
        return self.shiftoff

    # Set the shiftoff value
    def set_shiftoff(self, shiftoff):
        logging.info('Changing the shiftoff from %s to  %s', self.shiftoff, shiftoff)
        self.shiftoff = shiftoff
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)
        self.rtlsdr_source_0.set_center_freq(self.fc-self.shiftoff, 0)
        self.rtlsdr_source_0.set_bandwidth(250e3+abs(self.shiftoff), 0)

    # Get the current PPM value
    def get_ppm(self):
        return self.ppm

    # Set the PPM value
    def set_ppm(self, ppm):
        logging.info('Changing the PPM from %s to  %s', self.ppm, ppm)
        self.ppm = ppm
        self.rtlsdr_source_0.set_freq_corr(self.ppm, 0)

    # Get the current gain value
    def get_gain(self):
        return self.gain

    # Set the gain value
    def set_gain(self, gain):
        logging.info('Changing gain from %s to  %s', self.gain, gain)
        self.gain = gain
        self.rtlsdr_source_0.set_gain(self.gain, 0)

    # Get the listening frequency
    def get_fc(self):
        return self.fc

    # Set the frequency to listen
    def set_fc(self, fc):
        logging.info('Changing frequency from %s to %s', self.fc, fc)
        self.fc = fc
        self.rtlsdr_source_0.set_center_freq(self.fc-self.shiftoff, 0)

# Setup all arguments allowed to the command script and checking types
def setup_parameters():
    parser = argparse.ArgumentParser(description='Configure sniffing parameters')
    group = parser.add_argument_group("grgsm arguments")
    group.add_argument("-g", "--gain", help="Set the amplification value", default=30, type=float)
    group.add_argument("-p", "--ppm", help="Set PPM Stream Modulation value", default=0, type=int)
    group.add_argument("-s", "--samp_rate", help="Set the rate value of the antenna", default=2000000.052982, type=float)
    group.add_argument("-o", "--shiftoff", help="Set the shiftoff value", default=400000, type=float)
    group.add_argument("-f", "--frequencies", help="Set the list of frequencies to scan : 937000000 932950000 ...", default=[937700000], type=float, nargs='+')
    group.add_argument("-t", "--scan_time", help="Set the scan time for each frequency", default=2, type=float)
    group.add_argument("-n", "--repeat", help="Set the number of repeat of the scanning cycle", default=5, type=int)
    return parser

# Checking arguments values
def checking_arguments(frequencies, gain, ppm):
    if (ppm > 150 or ppm < -150):
        raise argparse.ArgumentTypeError("PPM value must be between -150 and 150 included")
    if (gain > 50 or gain < 0):
        raise argparse.ArgumentTypeError("Amplification (gain value) must be between 0 and 50 included")
    for fc in frequencies:
        if (fc <= 0):
            raise argparse.ArgumentTypeError("No frequency has negative or null value")

class sniffingHandler:

    def __init__(self, frequencies, gain, ppm, samp_rate, shiftoff):
        # Checking parameters values only (not type)
        checking_arguments(frequencies, gain, ppm)
        self.frequencies = frequencies
        self.gain = gain
        self.ppm = ppm
        self.samp_rate = samp_rate
        self.shiftoff = shiftoff
        self.tb = airprobe_rtlsdr(fc=self.frequencies[0], gain=self.gain, ppm=self.ppm, samp_rate=self.samp_rate, shiftoff=self.shiftoff)

    def start_sniffing(self):
        self.tb.start()

        # Launch gr-gsm in another thread to avoid putting the main process in "wait state"
        self.grgsm = Thread(target=self.tb.wait)
        self.grgsm.daemon = True # Stop the thread if the main process is stopped
        self.grgsm.start()

    # Loop to sniff on each specified frequencies
    def run_sniffing(self, repeat, scan_time):
        for i in range(1, repeat, scan_time):
            for fc in self.frequencies:
                #print("Scanning frequency : " + str(fc))
                self.tb.set_fc(fc)
                time.sleep(scan_time)

    # Stop sniffing process
    def stop_sniffing(self):
        self.tb.stop()

# Main function
if __name__ == '__main__':

    # Log system
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename='sniffing.log', filemod='w', level=logging.INFO)

    # Loading arguments parser
    parser = setup_parameters()

    # Getting all arguments in variable "args"
    args = parser.parse_args()

    # Checking arguments values
    checking_arguments(args.frequencies, args.gain, args.ppm)

    # Creating class to handle gr-gsm process
    handler = sniffingHandler(args.frequencies, args.gain, args.ppm, args.samp_rate, args.shiftoff)

    # Lanching sniffing until user stop it
    handler.start_sniffing()

    # Running function
    handler.run_sniffing(args.repeat, args.scan_time)

    # Stopping sniffing threads
    handler.stop_sniffing()

