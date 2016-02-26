#!/usr/bin/env python3.4

"""
    This module sends SMS from the fake BTS to
    the target mobile.
"""

from optparse import OptionParser
from badimsicore_openbts import BadimsicoreBtsService

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team"

class BadSMSSender:

    @staticmethod
    def send_sms(imsi_recipient, msisdn_sender, message):
        """
        send a sms using a fake BTS
        :param imsi_recipient:
        :param msisdn_sender:
        :param message:
        :return:
        """
        print("Sending to " + imsi_recipient + " from " + msisdn_sender + ": " + message)
        command = ["sendsms", imsi_recipient, msisdn_sender, message]
        BadimsicoreBtsService.send_command(command)


def main():
    parser = OptionParser(usage='Usage: %prog -r <recipient> -s <sender> -m <message>')
    parser.add_option('-r', '--recipient', dest='recipient', help='Recipient of the message')
    parser.add_option('-s', '--sender', dest='sender', help='Sender of the message')
    parser.add_option('-m', '--message', dest='message', help='Message to be sent (160 chars max.)')
    (options, args) = parser.parse_args()
    if options.recipient is None:
        parser.error("Recipient missing")
    elif options.sender is None:
        parser.error("Sender is missing")
    elif options.message is None:
        parser.error("Message is missing")
    elif options.message.__len__() > 160:
        parser.error("Message is too long")

    sms_sender = BadSMSSender()
    sms_sender.send_sms(options.recipient, options.sender, options.message)


if __name__ == '__main__':
    main()
