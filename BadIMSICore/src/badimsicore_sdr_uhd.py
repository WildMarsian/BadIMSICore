#!/usr/bin/python3.4

import os
import subprocess
from badimsicore_sdr_driver import BadIMSICoreSdrDriver

class BadIMSICoreUHDDriver(BadIMSICoreSdrDriver):

    def uhd_software_reconnect(self):
        """
            Detect and try to unbind then bind the UHD device
            Return: 
                -2 if there was a critical error with the UHD Device
                -1 if the device was not deteted by the system
                 0 if there was no problem
                 1 if the script didn't have root permission
                 2 if the IdProduct argument was empty or null
        """
        args = ["reload_usb_usrp.sh", "0020"]
        exit_code = subprocess.call(args, shell=True, stdout=subprocess.PIPE)
        if(exit_code == 0):
	    print("UHD device USB reload successful")
        return exit_code

    def uhd_check_downloaded_image(self):
        """
            Check if the two necessarily firmware are detected on the system
            Download all the fpga images linked to the uhd
            return: The command return value 0 if it is correct, -2 
        """
        if (not os.path.isfile("/usr/local/share/uhd/images/usrp_b200_fw.hex")):
            return -2
        if (not os.path.isfile("/usr/local/share/uhd/images/usrp_b210_fpga.bin")):
            return -2

        exit_code = subprocess.call(args="uhd_images_downloader", shell=True, stdout=subprocess.PIPE)
        if(exit_code == 0):
	    print("Downloading image to host - Download successful")
        return exit_code 

    def uhd_usrp_probe(self):
        """
            Load the image stored in the host to the device's firmware
            The 255 code is an error due to uhd_usrp_probe when the device is not found
            :return: 0 if the command is correctly launched another number otherwise
        """
        exit_code = subprocess.call(args="uhd_usrp_probe", stdout=subprocess.PIPE)
        if(exit_code == 0):
            print("Launching uhd_usrp_probe - Firmware loaded to the device")
        return exit_code

    def uhd_find_devices(self):
        """
            Check if the device is connected to the host
            :return: 0 if the command is correctly launched another number otherwise
        """
        exit_code = subprocess.call(args="uhd_find_devices", stdout=subprocess.PIPE)
        if(exit_code == 0):
            print("Launching uhd_find_devices - Device connected")
        return exit_code
            
    def init_bts(self):
        uhd_version=0020
        minimal_kernel="2.6.38"
        retry=6

        # Checking linux kernel version to allow usb enable/disable script
        kernel_info= os.uname()
        kernel_release = kernel_info[2]
        if (kernel_release < minimal_kernel)
            raise ValueError ("Kernel version not supported")
	
        state = self.uhd_check_downloaded_image()
        if (state != 0):
            print ("No firmware found, please download yourself the firmware or connect the system to internet")
            return state

        for cpt in range (1, retry):
            state = self.uhd_find_devices()
            if (state == 0):
                state = self.uhd_usrp_probe()
            
            if (state != 0):
                reload_usb = uhd_software_reconnect()
                if (reload_usb < 0):
                    print("Critical error with UHD Device, please disconnect manually then reconnect")
                if (reload_usb > 0):
                    print("Critical error, call without arguments or corrects rights")
                if (reload_usb != 0):
                    return reload_usb

        return state

