#!/usr/bin/python3.4

from badimsicore_sdr_driver import BadIMSICoreSdrDriver
import usb.core

class BadIMSICoreUHDDriver(BadIMSICoreSdrDriver):
    def init_bts(self, sdr_id):
        device = core.find(idVentor=0x2500, idProduct=sdr_id)
        if device is None:
            raise ValueError("Device not found")
        
        with open("output.txt", "w") as target_file:
            print("Device found", file=target_file)

        

if __name__ == '__main__':
    uhdHandler = BadIMSICoreUHDDriver()
    uhdHandler.init(0x0020)
        

# WarenUT
# vérifier connexion usb uhd lsusb
# on/off sur usb
# => attention au port && ID du uhd


# Alisterwan
# vérifier présence b210
# télécharger si nécessaire avec ihd donw
# uhd_usrp_probe et gestion erreurs avec boucle et cpt => retour utilisateur

