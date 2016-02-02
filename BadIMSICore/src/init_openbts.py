import subprocess
#to launch openBTS we need at least that sipauthserve and smqueue

class InitOpenBTS():
    # launch the sipauthserve service
    def init_sipauthserve(self):
        sortie = subprocess.call(args="start sipauthserve",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

    # stop the sipauthserve service
    def stop_sipauthserve(self):
        sortie = subprocess.call(args="stop sipauthserve",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

    # launch the smqueue service
    def init_smqueue(self):
        sortie = subprocess.call(args="start smqueue",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

    # stop the smqueue service
    def stop_smqueue(self):
        sortie = subprocess.call(args="stop smqueue",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

    # launch the fake bts transceiver
    def init_transceiver(self):
        sortie = subprocess.call(args="/OpenBTS/transceiver",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

    # launch the openbts console
    def init_openbts(self):
        sortie = subprocess.call(args="/OpenBTS/OpenBTS",shell=True, stdout=subprocess.PIPE)
        if sortie == 0:
            return True
        return False

# Main
def launch_openbts():
    init_openbts = InitOpenBTS()
    # Stop all the services first
    init_openbts.stop_sipauthserve()
    init_openbts.stop_smqueue()
    # Launch the two required services
    first = init_openbts.init_sipauthserve()
    second = init_openbts.init_smqueue()
    # checking if the two sub modules are enabled
    if first == True and second == True:
        third = init_openbts.init_transceiver()
        fourth = init_openbts.init_openbts()
        if(third==True and fourth==True):
            # we can launch openbts command here
            return True
        else:
            return False

if __name__ == '__main__':
    launch_openbts()