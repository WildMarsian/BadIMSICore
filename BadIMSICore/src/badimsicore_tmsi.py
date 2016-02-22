#!/usr/bin/python3.4
from badimsicore_openbts import BadimsicoreBtsService

class BadIMSICoreTIMSI:
    @staticmethod
    def get_all_timsi():
        command = ["tmsis"]
        BadimsicoreBtsService.send_command(command)

if __name__ == '__main__':
    timsi = BadIMSICoreTIMSI()
    return timsi.get_all_timsi()
