#!/usr/bin/env python3.4

"""
    BadIMSICoreUHDDriver attempts to load the UHD driver
    on the SDR card, using an USB connection. Sometimes,
    when the card is mount, the connection is lost. The goal
    of this module consists of establishing the connection.
"""

import os
import time
import subprocess
from badimsicore_sdr_driver import BadIMSICoreSdrDriver

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team"

class BadIMSICoreUHDDriver(BadIMSICoreSdrDriver):

    def uhd_software_reconnect(self, uhd_version):
        """
            Detect and try to unbind then bind the UHD device
            :return :
                -2 if there was a critical error with the UHD Device
                -1 if the device was not deteted by the system
                 0 if there was no problem
                 1 if the script didn't have root permission
                 2 if the IdProduct argument was empty or null
        """
        args = ["badimsicore_reload_usb_usrp", uhd_version]
        exit_code = subprocess.call(args)
        if (exit_code == 0):
            print("UHD device USB reload successful")
        return exit_code

    def uhd_check_downloaded_image(self):
        """
            Check if the two necessarily firmware are detected on the system
            Download all the fpga images linked to the uhd
            return: The command return value 0 if it is correct, -2 
        """
        all_files_here = True
        if (os.path.isfile("/usr/local/share/uhd/images/usrp_b200_fw.hex") is False):
            all_files_here = False
        if (os.path.isfile("/usr/local/share/uhd/images/usrp_b210_fpga.bin") is False):
            all_files_here = False
        if (all_files_here):
            return 0
        
        exit_code = subprocess.call(args="uhd_images_downloader")
        if (exit_code == 0):
            print("Downloading image to host - Download successful")
        return exit_code 

    def uhd_usrp_probe(self):
        """
            Load the image stored in the host to the device's firmware
            The 255 code is an error due to uhd_usrp_probe when the device is not found
            :return: 0 if the command is correctly launched another number otherwise
        """
        exit_code = subprocess.call(args="uhd_usrp_probe")
        if (exit_code == 0):
            print("Launching uhd_usrp_probe - Firmware loaded to the device")
        return exit_code

    def uhd_find_devices(self):
        """
            Check if the device is connected to the host
            :return: 0 if the command is correctly launched another number otherwise
        """
        exit_code = subprocess.call(args="uhd_find_devices")
        if (exit_code == 0):
            print("Launching uhd_find_devices - Device connected")
        return exit_code
            
    def init_bts(self):
        """
    		Initialize the SDR connection with the host.
    		:return :
    		-2 if there was a critical error with the UHD Device
                -1 if the device was not deteted by the system
                 0 if there was no problem
                 1 if the script didn't have root permission
                 2 if the IdProduct argument was empty or null
    	"""
        uhd_version="0020"
        minimal_kernel="2.6.38"
        retry=6
        waiting_time=20

        print ("Waiting "+ str(waiting_time) + "s before trying loading the firware")

        print ("Checking linux kernel version to allow usb enable/disable script")
        kernel_info= os.uname()
        kernel_release = kernel_info[2]
        if (kernel_release < minimal_kernel):
            raise ValueError ("Kernel version not supported")
	
        print ("Checking if firmwares were downloaded on the system")
        state = self.uhd_check_downloaded_image()
        if (state != 0):
            print ("No firmware found, please download yourself the firmware or connect the system to internet")
            return state

        for cpt in range (1, retry):
            print ("Attempt " + str(cpt) + " to load UHD device USB")
            state = self.uhd_find_devices()
            if (state == 0):
                state = self.uhd_usrp_probe()
            
            if (state != 0):
                print ("Script unable to detect the UHD, trying to reboot the device")
                state = self.uhd_software_reconnect(uhd_version)
                if state < 0:
                    print("Device failed, please disconnect it then retry")
                    return state
                else:
                    time.sleep(6)
            else:
                break
        return state

if __name__ == '__main__':
    print ("This script NEEDS root rights")
    uhd_handler = BadIMSICoreUHDDriver()
    uhd_handler.init_bts()

