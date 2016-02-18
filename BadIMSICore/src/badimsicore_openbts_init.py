#!/usr/bin/python3.4

import subprocess
import time
#to launch openBTS we need at least that sipauthserve and smqueue

class InitOpenBTS:


    # launch the sipauthserve service
    @staticmethod
    def init_sipauthserve():
        sortie = subprocess.call(args="start sipauthserve",shell=True, stdout=subprocess.PIPE)
        return sortie == 0

    # stop the sipauthserve service
    @staticmethod
    def stop_sipauthserve():
        sortie = subprocess.call(args="stop sipauthserve",shell=True, stdout=subprocess.PIPE)
        return sortie == 0

    # launch the smqueue service
    @staticmethod
    def init_smqueue():
        exit_code = subprocess.call(args="start smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # stop the smqueue service
    @staticmethod
    def stop_smqueue():
        exit_code = subprocess.call(args="stop smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # launch the fake bts transceiver
    @staticmethod
    def init_transceiver():
        exit_code = subprocess.Popen(args="/OpenBTS/transceiver")
        return exit_code == 0

    # launch the openbts service
    @staticmethod
    def init_openbts():
        exit_code = subprocess.call(args="start openbts", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # stop the openbts service and fake bts transceiver
    @staticmethod
    def stop_openbts():
        exit_code = subprocess.call(args="stop openbts", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

def init_openbts():
    # Stop all the services first
    o = InitOpenBTS()
    o.stop_sipauthserve()
    o.stop_smqueue()
    o.stop_openbts()
    # Launch the two required services
    o.init_sipauthserve()
    o.init_smqueue()
    o.init_transceiver()
    time.sleep(7)
    o.init_openbts()
    
if __name__ == '__main__':
    init_openbts()
