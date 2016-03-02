#!/usr/bin/env python3.4

"""
This class is used to control the openbts service
You need to construct the new instance using the method get_badimsicore_bts_service(exec_context)
"""

import subprocess
import os
import sys
import argparse
import time
import locale
from badimsicore_openbts_init import InitOpenBTS
from badimsicore_sdr_uhd import BadIMSICoreUHDDriver
from bts import BTS
from badimsicore_openbts_config import BadimsicoreBtsConfig

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team" 

class BadimsicoreBtsService:
        
    def start(self, ci=None, lac=None, mnc=None, mcc=None, open_registration=None, message_registration=None):
        """
        Start openbts services. Default values are those defined in the OpenBTS database file. 
        :param ci: The Cell ID
        :param lac: The Location Area Code
        :param mnc: The Mobile Network Code
        :param mcc: The Mobile Country Code
        :param open_registration: 
        :param message_resgistration: The message sent to the mobile when it is resgistered to the fake network
        :return: None
        """
        #Stop openbts services
        self.stop()

        # Destruction of sms files
        smslog1 = "/var/log/smslog"
        smslog2 = "/var/log/smslog.offset"

        subprocess.call(["dd", "if=/dev/null", "of=/var/log/syslog"])
        try:
            os.remove(smslog1)
            os.remove(smslog2)
        except OSError:
            pass

        #SDR
        uhd_handler = BadIMSICoreUHDDriver()
        init_bts = uhd_handler.init_bts()
        if init_bts == 0:
            #Config OpenBTS.db
            openbtsdb = '/etc/OpenBTS/OpenBTS.db'
            badimsicore_bts_config = BadimsicoreBtsConfig(openbtsdb)
            if ci and lac and mnc and mcc:
                bts = BTS(mcc, mnc, lac, ci)
                # inject bts params into OpenBTS                
                badimsicore_bts_config.update_badimsicore_bts_config(bts)
            elif open_registration:
                badimsicore_bts_config.update_database("Control.LUR.OpenRegistration", open_registration)
            elif message_registration:
                badimsicore_bts_config.update_database("Control.LUR.OpenRegistration.Message", message_registration)
            badimsicore_bts_config.close()
            #Start openbts services
            InitOpenBTS.init_sipauthserve()
            InitOpenBTS.init_smqueue()
            InitOpenBTS.init_transceiver()
            time.sleep(7)
            InitOpenBTS.init_openbts()

    def stop(self):
        """
        Stop openbts services
        :return: None
        """
        InitOpenBTS.stop_openbts()
        InitOpenBTS.stop_smqueue()
        InitOpenBTS.stop_sipauthserve()
    
    @staticmethod
    def status():
        """
        Check if openbts service is started
        :return: 0 if OpenBTS is running, otherwise 
        """
        encoding = locale.getdefaultlocale()[1]
        p = subprocess.Popen(['status', 'openbts'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        stdout = out.decode(encoding)
        if 'process' in stdout: 
            return 0
        else:
            return 1
        
    @staticmethod
    def send_command(command):
        """
        BadimsicoreBtsService send a command to openbts,
        Using OpenBTSDo utility.
        :command a list of string corresponding to the command fragment (split(" "))
        """
        openbts=["/OpenBTS/OpenBTSDo", "-c"]
        openbts.extend(command)
        p = subprocess.Popen(openbts)
        out, err = p.communicate()
        return out


def main():
    service = BadimsicoreBtsService()
    #Main parser
    parser = argparse.ArgumentParser(description='Usage of openbts')
    #Subparsers
    subparsers = parser.add_subparsers(dest='subparser_name')
    #Subparser start_parser
    start_parser = subparsers.add_parser('start', help='Start openbts')
    start_parser.set_defaults(func=service.start)
    start_parser.add_argument('-i', '--ci',  dest='ci', help='The Cell ID of the cell')
    start_parser.add_argument('-l', '--lac', dest='lac', help='The LAC of the cell')
    start_parser.add_argument('-n', '--mnc', dest='mnc', help='The Mobile Network Code of the cell. Must have 2 digits')
    start_parser.add_argument('-c', '--mcc', dest='mcc', help='The Mobile Country Code of the cell. Must have 3 digits')
    start_parser.add_argument('-m', '--message-registration', dest='message_registration', help='The message upon registration of a mobile in the fake network', default="")
    start_parser.add_argument('-p', '--open-registration', dest='open_registration', help='The access authorization for the registration on the fake network', default=".*")
    #Subparser stop_parser 
    stop_parser = subparsers.add_parser('stop', help='Stop openbts')
    stop_parser.set_defaults(func=service.stop)

    args = parser.parse_args()
    if args.subparser_name == 'start':
        if args.ci and (not args.ci.isnumeric() or int(args.ci) < 0 or int(args.ci) > 65535):
            print(int(args.ci))
            sys.exit("Error : Cell ID must be a number betwen 0 and 65535")
        if args.lac and not args.lac.isnumeric():
            sys.lac("Error : LAC must be a number")
        if args.mcc and (len(args.mcc) != 3 or not args.mcc.isnumeric()):
            sys.exit("Error : mcc must have 3 digits")
        if args.mnc and (len(args.mnc) != 2 or not args.mcc.isnumeric()):
            sys.exit("Error : mnc must have 2 digits")
        args.func(args.ci, args.lac, args.mnc, args.mcc, args.open_registration, args.message_registration)
    elif args.subparser_name == 'stop':
        args.func()

if __name__ == '__main__':
    main()
