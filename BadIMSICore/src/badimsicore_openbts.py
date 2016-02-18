#!/usr/bin/python3.4

import subprocess
import argparse
import time
from badimsicore_openbts_init import InitOpenBTS

"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService:
        
    def start(self):
        #Stop openbts services
        self.stop()        
        #SDR
        #Config OpenBTS.db
        #Start openbts services
        InitOpenBTS.init_sipauthserve()
        InitOpenBTS.init_smqueue()
        InitOpenBTS.init_transceiver()
        time.sleep(7)
        InitOpenBTS.init_openbts()

    def stop(self):
        InitOpenBTS.stop_openbts()
        InitOpenBTS.stop_smqueue()
        InitOpenBTS.stop_sipauthserve()    
    
    @staticmethod
    def send_command(command):
        """BadimsicoreBtsService send a command to openbts
        :command a list of string corresponding to the command fragment (split(" "))
        """
        openbts=["/OpenBTS/OpenBTSDo", "-c"]
        openbts.extend(command)
        p = subprocess.Popen(openbts)
        return p.communicate()


def main():
    service = BadimsicoreBtsService()
    #Main parser    
    parser = argparse.ArgumentParser(description='Usage of openbts')
    #Subparsers
    subparsers = parser.add_subparsers()
    #Subparser start_parser
    start_parser = subparsers.add_parser('start', help='Start openbts')
    start_parser.ad
    start_parser.set_defaults(func=service.start)    
    #Subparser stop_parser    
    stop_parser = subparsers.add_parser('stop', help='Stop openbts')
    stop_parser.set_defaults(func=service.stop)
    
    args = parser.parse_args()
    args.func()

if __name__ == '__main__':
    main()
