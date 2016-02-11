#!/usr/bin/python3.4

import subprocess
#to launch openBTS we need at least that sipauthserve and smqueue

class InitOpenBTS:

    def __init__(self):
        pass


    # launch the sipauthserve service
    def init_sipauthserve(self):
        sortie = subprocess.call(args="start sipauthserve",shell=True, stdout=subprocess.PIPE)
        return sortie == 0

    # stop the sipauthserve service
    def stop_sipauthserve(self):
        sortie = subprocess.call(args="stop sipauthserve",shell=True, stdout=subprocess.PIPE)
        return sortie == 0

    # launch the smqueue service
    def init_smqueue(self):
        exit_code = subprocess.call(args="start smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # stop the smqueue service
    def stop_smqueue(self):
        exit_code = subprocess.call(args="stop smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # launch the fake bts transceiver
    def init_transceiver(self):
        exit_code = subprocess.call(args="/OpenBTS/transceiver", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    # launch the openbts console
    def init_openbts(self):
        exit_code = subprocess.call(args="/OpenBTS/OpenBTS", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

def launch_openbts():
    # Stop all the services first
    o = InitOpenBTS()
    o.stop_sipauthserve()
    o.stop_smqueue()
    # Launch the two required services
    first = o.init_sipauthserve()
    second = o.init_smqueue()
    # checking if the two sub modules are enabled
    if first and second:
        third = o.init_transceiver()
        fourth = o.init_openbts()
        if third and fourth:
            # we can launch openbts command here
            return True
        else:
            return False

if __name__ == '__main__':
    launch_openbts()
