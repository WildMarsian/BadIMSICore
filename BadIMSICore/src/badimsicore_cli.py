import argparse
parser = argparse.ArgumentParser()

fncGroup = parser.add_mutually_exclusive_group()

# badimsicli -i sdrDevice
parser.add_argument("-i", "--init", help="search the SDR given in parameters and configure it if necessary",
                    action="store_true")

# badimsicli -s
parser.add_argument("-s", "--sniff", help="Display the list of cells at range",
                    action="store_true")

# badimsicli -l
parser.add_argument("-l", "--listsms", help="List sms that have been recieved ",
                    action="store_true")

# badimsicli -j start/stop/status
parser.add_argument("-j", "--jamming", help="lance le brouillage sur la bande de fréquence donnée en paramètre",
                    choices=["start", "stop", "status"])

# badimsicli -d device
parser.add_argument("-d", "--device", help="force l'utilisation du sdr fournit au lieu du sdr paramétré "
                                           "dans le fichier de configuration")

# badimsicli -b start/stop/restart/status
parser.add_argument("-b", "--bts", help="start the bts using the config /etc/badimsibox/bts.conf",
                    choices=["start", "stop", "restart", "status"])

# [-c[=btsConfigFilePath]]
parser.add_argument('-c', '--config', default= "/etc/badimsicore/btsconfig.conf",
                   help='A BadIMSIBox config file')

# badimsicli btsConfigFilePath
parser.add_argument("-c", "--config", help="force le fichier de configuration de de fake BTS à utiliser")

args = parser.parse_args()
print(args.init)