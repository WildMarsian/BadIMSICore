#!/usr/bin/python3.4
from badimsicore_openbts import BadimsicoreBtsService

class BadIMSICoreTIMSI:
    @staticmethod
    def get_all_timsi():
        command = ["timsi"]
        BadimsicoreBtsService.send_command(command)

if __name__ == '__main__':
    timsi = BadIMSICoreTIMSI()
    timsi.get_all_timsi()

