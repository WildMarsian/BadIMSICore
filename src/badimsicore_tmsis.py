#!/usr/bin/env python3.4

"""
    This class gets current tmsis registered on the BTS.
"""

import sys
from badimsicore_openbts import BadimsicoreBtsService

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team"

class BadIMSICoreTIMSI:
    
    @staticmethod
    def get_all_timsi():
        """
            Gets all tmsis registered on the BTS.
            :returns: the string representation of tmsis table
        """
        if BadimsicoreBtsService.status() == 0:
            command = ["tmsis"]
            return BadimsicoreBtsService.send_command(command)
        else:
            print("Openbts is not launch", file=sys.stderr)

if __name__ == '__main__':
    timsi = BadIMSICoreTIMSI()
    print(timsi.get_all_timsi())
    exit(0)
