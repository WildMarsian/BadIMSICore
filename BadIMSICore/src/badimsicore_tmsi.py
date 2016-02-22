#!/usr/bin/python3.4
from badimsicore_openbts import BadimsicoreBtsService
import sys

class BadIMSICoreTIMSI:
    @staticmethod
    def get_all_timsi():
        if BadimsicoreBtsService.status() == 0:
            command = ["tmsis"]
            BadimsicoreBtsService.send_command(command)
        else:
            print("Openbts is not launch", file=sys.stderr)

if __name__ == '__main__':
    timsi = BadIMSICoreTIMSI()
    timsi.get_all_timsi()

