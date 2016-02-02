import os
import subprocess
from multiprocessing import Process, Pipe

std_out_file = "teststdout"
std_in_file = "teststdin"

try:
    os.mkfifo(std_out_file)
    os.mkfifo(std_in_file)
except RuntimeError as err:
    print("Failed to create FIFO: %s" % err)
else:
    fifo_out = open(std_out_file, 'w')
    fifo_in = open(std_in_file, 'r')
    p = subprocess.popen(["bc"], stdout=fifo_out, stdin=fifo_in, stderr=fifo_out)
    p.comunicate()

fifo_out.close()
fifo_in.close()
os.remove(std_in_file)
os.remove(std_out_file)
