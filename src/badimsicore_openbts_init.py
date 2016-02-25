#!/usr/bin/env python3.4

"""
    This module initializes OpenBTS by launching services and
    its dependencies.
    
    Needed services are restarted automatically by the function
    init_openbts().
    
    Services are :
    - sipauthserve
    - smqueue
    - transceiver
    - openbts
"""

import subprocess
import time


__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team" 

class InitOpenBTS:

    @staticmethod
    def init_sipauthserve():
        """
            Start sipauthserve service in an other process.
            :return: True if the process has successfully launched,
            otherwise return False
        """
        exit_code = subprocess.call(args="start sipauthserve",shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    @staticmethod
    def stop_sipauthserve():
        """
            Stop sipauthserve service.
            :return: True if the process has successfully stopped,
            otherwise return False
        """
        exit_code = subprocess.call(args="stop sipauthserve",shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    @staticmethod
    def init_smqueue():
        """
            Start smqueue service in an other process.
            :return: True if the process has successfully launched,
            otherwise return False
        """
        exit_code = subprocess.call(args="start smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    @staticmethod
    def stop_smqueue():
        """
            Stop smqueue service.
            :return: True if the processe has successfully stopped,
            otherwise return False
        """
        exit_code = subprocess.call(args="stop smqueue", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0


    @staticmethod
    def init_transceiver():
        """
            Start transceiver service in an other process.
            :return: True if the process has successfully launched,
            otherwise return False
            
            Here subprocess.Popen() is used because transceiver is
            launched in the background, so without exit return code in
            the nominal case.
        """
        exit_code = subprocess.Popen(args="/OpenBTS/transceiver")
        return exit_code == 0

    @staticmethod
    def init_openbts():
        """
            Start openbts service in an other process.
            :return: True if the process has successfully launched,
            otherwise return False
        """
        exit_code = subprocess.call(args="start openbts", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

    @staticmethod
    def stop_openbts():
        """
            Stop openbts service in an other process.
            :return: True if the process has successfully launched,
            otherwise return False
            
            Note that transceiver service will be also stopped by calling
            this function (openbts usage).
        """
        exit_code = subprocess.call(args="stop openbts", shell=True, stdout=subprocess.PIPE)
        return exit_code == 0

def init_openbts():
    # Stop all the services first
    o = InitOpenBTS()
    o.stop_sipauthserve()
    o.stop_smqueue()
    o.stop_openbts()
    # Launch the two required services
    o.init_sipauthserve()
    o.init_smqueue()
    o.init_transceiver()
    # This sleep is needed for environement
    # reasons : on a virtual machine, initialization
    # of transceiver service takes few seconds, so
    # openbts need to wait.
    time.sleep(7)
    o.init_openbts()
    
if __name__ == '__main__':
    init_openbts()
