
import os
import subprocess
from daemon import Daemon


def get_badimsicore_bts_service():
    std_out_file = "teststdout"
    std_in_file = "teststdin"
    std_err_file = "teststderr"

    try:
        os.mkfifo(std_out_file)
        os.mkfifo(std_in_file)
        os.mkfifo(std_err_file)

        service = BadimsicoreBtsService("badimsicore_bts.pid", std_out_file, std_in_file, std_err_file)
        service.start()

    except IOError as ioErr:
        print("IO error : unable tu create named pipe (might be impossible on windows) : %s\n", ioErr)


class BadimsicoreBtsService(Daemon):

    def run(self):
        p = subprocess.Popen("bc", stdout=self.stdout, stdin=self.stdin, stderr=self.stderr)
        p.communicate()
