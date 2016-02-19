#!/usr/bin/python3.4

import subprocess

class BadIMSICoreUHDChecker():

# Alisterwan
# vérifier présence b210
# télécharger si nécessaire avec ihd donw
# uhd_usrp_probe et gestion erreurs avec boucle et cpt => retour utilisateur

	def uhd_find_devices(self):
		"""
			Check if the device is connected to the host
			:return: 0 if the command is correctly launched another number otherwise
		"""
		exit_code = subprocess.call(args="uhd_find_devices", stdout=subprocess.PIPE)
		if(exit_code == 0):
			print("Launching uhd_find_devices - Device connected")
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

	def uhd_images_downloader(self):
		"""
			Download all the fpga images linked to the uhd
			return: The command return value 0 if it is correct.
		"""
		exit_code = subprocess.call(args="uhd_images_downloader", shell=True, stdout=subprocess.PIPE)
		if(exit_code == 0):
			print("Downloading image to host - Download sucessful")
		return exit_code

	def check_if_uhd_is_launch(self,delay):
		print("Attempting to connect until ",delay-1," time(s)")		
		for cpt in range(1,delay):
			print("Attempt",cpt)			
			state = self.uhd_find_devices()
			if(state == 0):
				probe_state = self.uhd_usrp_probe()
				if(probe_state == 0):
					print("Everything is fine ! - We can use the device ")
					return 0
			else:
				reload_state = self.uhd_images_downloader()
				if(reload_state == 0):
					return 0
		print("You must unplug and replug the UHD")

if __name__ == '__main__':
    uhdHandler = BadIMSICoreUHDChecker()
    uhdHandler.check_if_uhd_is_launch(6)
    

# WarenUT
# vérifier connexion usb uhd lsusb
# on/off sur usb
# => attention au port && ID du uhd


