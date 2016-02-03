
import os
import subprocess
from daemon import Daemon


class BadimsicoreBtsService(Daemon):

    def run(self):
        p = subprocess.Popen("bc", stdout=self.stdout, stdin=self.stdin, stderr=self.stderr)
        p.communicate()

    @staticmethod
    def get_badimsicore_bts_service(exec_context):
        std_out_file = os.path.join(exec_context, "bbts_stdout")
        std_in_file = os.path.join(exec_context, "bbts_stdin")
        std_err_file = os.path.join(exec_context, "bbts_stderr")
        pid_file = os.path.join(exec_context, "badimsicore_bts.pid")

        if not os.path.isfile(pid_file):
            try:
                os.mkfifo(std_out_file)
                os.mkfifo(std_in_file)
                os.mkfifo(std_err_file)
                return BadimsicoreBtsService(pid_file, std_out_file, std_in_file, std_err_file)

            except IOError as ioErr:
                print("IO error : unable tu create named pipe (might be impossible on windows) : %s\n", ioErr)

            return BadimsicoreBtsService(pid_file, std_out_file, std_in_file, std_err_file)
