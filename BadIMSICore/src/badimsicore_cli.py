import argparse
parser = argparse.ArgumentParser()

fncGroup = parser.add_mutually_exclusive_group()

# badimsicli -i sdrDevice
fncGroup.add_argument("-i", "--init", help="search the SDR given in parameters and configure it if necessary",
                      action="store_true")

# badimsicli -l
fncGroup.add_argument("-l", "--listen", help="Display the list of cells at range",
                      action="store_const", nargs="+", metavar="FREQUENCY")

# badimsicli -L
fncGroup.add_argument("-L", "--listsms", help="List sms that have been recieved ",
                      action="store_true")

# badimsicli -s [destination_IMSI] [sender_msisdn] [message]
fncGroup.add_argument("-s", "--send-sms", help="Send a SMS",
                      action="store_const", nargs=3, metavar=["[destination_IMSI]", "[sender_msisdn]", "[message]"])

# badimsicli -j start/stop/status
fncGroup.add_argument("-j", "--jamming", help="lance le brouillage sur la bande de fréquence donnée en paramètre",
                      choices=["start", "stop", "status"])

# badimsicli -d device
parser.add_argument("-d", "--device", help="force l'utilisation du sdr fournit au lieu du sdr paramétré "
                                           "dans le fichier de configuration")

# badimsicli -b start/stop/restart/status
fncGroup.add_argument("-b", "--bts", help="start the bts using the config /etc/badimsibox/bts.conf",
                    choices=["start", "stop", "restart", "status"])

# [-c[=btsConfigFilePath]]
parser.add_argument('-c', '--config', default= "/etc/badimsicore/btsconfig.conf",
                   help='Start badimsicore bts service using')

# badimsicli btsConfigFilePath
parser.add_argument("-c", "--config", help="force le fichier de configuration de de fake BTS à utiliser")

args = parser.parse_args()



