#!/usr/bin/python3.4

import subprocess
import argparse
import time
from badimsicore_openbts_init import InitOpenBTS
from badimsicore_openbts_config import BadimsicoreBtsConfig
"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService:
        
    def start(self, operator=None, ci=None, lac=None, mnc=None, mcc=None, message_registration=None):
        #Stop openbts services
        self.stop()        
        #SDR
        #Config OpenBTS.db
        if operator
            
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
    subparsers = parser.add_subparsers(dest='subparser_name')
    #Subparser start_parser
    start_parser = subparsers.add_parser('start', help='Start openbts')
    start_parser.set_defaults(func=service.start)
    start_parser.add_argument('-o', '--operator', dest='operator', help='A String of the gsm operator')
    start_parser.add_argument('-i', '--ci',  dest='ci', type=int, help='The ci of the cell')
    start_parser.add_argument('-l', '--lac', dest='lac', type=int, help='The lac of the cell')   
    start_parser.add_argument('-m', '--mnc', dest='mnc', type=int, help='The Mobile Network Code of the cell')
    start_parser.add_argument('-c', '--mcc', dest='mcc', type=int, help='The Mobile Country Code of the cell')
    start_parser.add_argument('-m', '--message-registration', dest='message_registration', type=int, help='The message upon registration of a mobile in the fake network')    
    #Subparser stop_parser 
    stop_parser = subparsers.add_parser('stop', help='Stop openbts')
    stop_parser.set_defaults(func=service.stop)
    
    if args.subparser_name == 'start':    
        args.func(args.operator, args.ci, args.lac, args.mnc, args.mcc, args.message_registration)
    elif args.subparser_name == 'stop':
        args.func()

if __name__ == '__main__':
    main()
