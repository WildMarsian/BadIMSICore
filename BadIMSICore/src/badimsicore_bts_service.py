
import os
import subprocess
from daemon import Daemon


class BadimsicoreBtsService(Daemon):
    
    def __init__(self, pidfile):
        super(BadimsicoreBtsService, self).__init__(pidfile)

    def run(self):
        subprocess.Popen(["/OpenBts/OpenBts"])

    @staticmethod
    def get_badimsicore_bts_service(exec_context):
        pid_file = os.path.join(exec_context, "badimsicore_bts.pid")
        return BadimsicoreBtsService(pid_file)

    @staticmethod
    def send_command(command):
        openbts=["/OpenBts/OpenBtsDo", "-c"]
        p = subprocess.Popen(openbts.extend(command))
        return p.communicate()

