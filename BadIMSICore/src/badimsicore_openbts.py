#!/usr/bin/python3.4

import subprocess
import argparse
import time
from badimsicore_openbts_init import InitOpenBTS
from badimsicore_sdr_uhd import BadIMSICoreUHDDriver
from bts import BTS

from badimsicore_openbts_config import BadimsicoreBtsConfig
"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""
class BadimsicoreBtsService:
        
    def start(self, ci=None, lac=None, mnc=None, mcc=None, message_registration=None):
        #Stop openbts services
        self.stop()
        #SDR
        uhd_handler = BadIMSICoreUHDDriver()
        uhd_handler.init_bts()
        #Config OpenBTS.db
        if ci and lac and mnc and mcc:
            bts = BTS(mcc, mnc, lac, ci)
            # inject bts params into OpenBTS
            openbtsdb = '../test/resources/clean/OpenBTS.db'
            badimsicore_bts_config = BadimsicoreBtsConfig(openbtsdb)
            badimsicore_bts_config.update_badimsicore_bts_config(bts)

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
    start_parser.add_argument('-i', '--ci',  dest='ci', help='The ci of the cell')
    start_parser.add_argument('-l', '--lac', dest='lac', help='The lac of the cell')
    start_parser.add_argument('-n', '--mnc', dest='mnc', help='The Mobile Network Code of the cell')
    start_parser.add_argument('-c', '--mcc', dest='mcc', help='The Mobile Country Code of the cell')
    start_parser.add_argument('-m', '--message-registration', dest='message_registration', help='The message upon registration of a mobile in the fake network')
    #Subparser stop_parser 
    stop_parser = subparsers.add_parser('stop', help='Stop openbts')
    stop_parser.set_defaults(func=service.stop)

    args = parser.parse_args()
    if args.subparser_name == 'start':    
        args.func(args.ci, args.lac, args.mnc, args.mcc, args.message_registration)
    elif args.subparser_name == 'stop':
        args.func()

if __name__ == '__main__':
    main()
