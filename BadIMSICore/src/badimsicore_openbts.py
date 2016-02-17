

import subprocess

"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService:

    def __init(self, sdrDriver):
        sdrDriver.initSDR()

    def start(self):
        """
        Start the daemon
        """
        subprocess.call(args="start openbts")

    def stop(self):
        """
        Stop the daemon
        """
        subprocess.call(args="stop openbts")

    def restart(self):
        """
        Restart the daemon
        """
        subprocess.call(args="restart openbts")

    def status(self):
        """
        return the status of the daemon
        """
        return subprocess.call(args="status openbts")

    @staticmethod
    def get_badimsicore_bts_service():
        """
        BadimsicoreBtsService factory
        :exec_context a string corresponding to the path of the context (the place where the pid file is stored)
        """
        return BadimsicoreBtsService()


    @staticmethod
    def send_command(command):
        """BadimsicoreBtsService send a command to openbts
        :command a list of string corresponding to the command fragment (split(" "))
        """
        openbts=["/OpenBts/OpenBtsDo", "-c"]
        openbts.extend(command)
        p = subprocess.Popen(openbts)
        return p.communicate()

    # launch the sipauthserve service
    @staticmethod
    def init_sipauthserve(self):
        sortie = subprocess.call(args="start sipauthserve", stdout=subprocess.PIPE)
        return sortie == 0

    # stop the sipauthserve service
    @staticmethod
    def stop_sipauthserve(self):
        sortie = subprocess.call(args="stop sipauthserve", stdout=subprocess.PIPE)
        return sortie == 0

    # launch the smqueue service
    @staticmethod
    def init_smqueue(self):
        exit_code = subprocess.call(args="start smqueue", stdout=subprocess.PIPE)
        return exit_code == 0

    # stop the smqueue service
    @staticmethod
    def stop_smqueue(self):
        exit_code = subprocess.call(args="stop smqueue",  stdout=subprocess.PIPE)
        return exit_code == 0

    @staticmethod
    def init_openbts():
        #TODO fix static to class
        # Stop all the services first
        BadimsicoreBtsService.stop_sipauthserve()
        BadimsicoreBtsService.stop_smqueue()
        # load the firmware
        BadimsicoreBtsService.load_firmware()
        # Launch the two required services
        first = BadimsicoreBtsService.init_sipauthserve()
        second = BadimsicoreBtsService.init_smqueue()
        # checking if the two sub modules are enabled
        return first and second and BadimsicoreBtsService.start()