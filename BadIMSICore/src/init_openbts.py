#/usr/bin/python

import subprocess


#to launch openBTS we need at least that sipauthserve and smqueue

# launch the sipauthserve service
def init_sipauthserve():
    sortie = subprocess.call(args="start sipauthserve",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return 1
    return 0

# stop the sipauthserve service
def stop_sipauthserve():
    sortie = subprocess.call(args="stop sipauthserve",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return True
    return False

# launch the smqueue service
def init_smqueue():
    sortie = subprocess.call(args="start smqueue",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return True
    return False

# stop the smqueue service
def stop_smqueue():
    sortie = subprocess.call(args="stop smqueue",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return True
    return False

# launch the fake bts transceiver
def init_transceiver():
    sortie = subprocess.call(args="/OpenBTS/transceiver",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return True
    return False

# launch the openbts console
def init_openbts():
    sortie = subprocess.call(args="/OpenBTS/OpenBTS",shell=True, stdout=subprocess.PIPE)
    if sortie == 0:
        return True
    return False



def launch_openbts():
    # Stop all the services first
    stop_sipauthserve()
    stop_smqueue()
    # Launch the two required services
    first = init_sipauthserve()
    second = init_smqueue()
    # checking if the two sub modules are enabled
    if first == True and second == True:
        third = init_transceiver()
        fourth = init_openbts()
        if(third==True and fourth==True):
            # we can launch openbts command here
            return True
        else:
            return False


launch_openbts()


