
import os
import subprocess

"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService:

    def start(self):
        """
        Start the daemon
        """
        subprocess.Popen(["start openbts"])

    def stop(self):
        """
        Stop the daemon
        """
        subprocess.Popen(["stop openbts"])

    def restart(self):
        """
        Restart the daemon
        """
        subprocess.Popen(["restart openbts"])

    def status(self):
        """
        return the status of the daemon
        """

    @staticmethod
    def get_badimsicore_bts_service(exec_context):
        """
        BadimsicoreBtsService factory
        :exec_context a string corresponding to the path of the context (the place where the pid file is stored)
        """
        pid_file = os.path.join(exec_context, "badimsicore_bts.pid")
        return BadimsicoreBtsService(pid_file)


    @staticmethod
    def send_command(command):
        """BadimsicoreBtsService send a command to openbts
        :command a list of string corresponding to the command fragment (split(" "))
        """
        openbts=["/OpenBts/OpenBtsDo", "-c"]
        openbts.extend(command)
        p = subprocess.Popen(openbts)
        return p.communicate()

