
import os
import subprocess
from daemon import Daemon

"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService(Daemon):
    
    def __init__(self, pidfile):
        super(BadimsicoreBtsService, self).__init__(pidfile)

    def run(self):
        subprocess.Popen(["/OpenBts/OpenBts"])
    """
    BadimsicoreBtsService factory
    :exec_context a string corresponding to the path of the context (the place where the pid file is stored)
    """
    @staticmethod
    def get_badimsicore_bts_service(exec_context):
        pid_file = os.path.join(exec_context, "badimsicore_bts.pid")
        return BadimsicoreBtsService(pid_file)

    """BadimsicoreBtsService send a command to openbts
    :command a list of string corresponding to the command fragment (split(" "))
    """
    @staticmethod
    def send_command(command):
        openbts=["/OpenBts/OpenBtsDo", "-c"]
        openbts.extend(command)
        p = subprocess.Popen(openbts)
        return p.communicate()

