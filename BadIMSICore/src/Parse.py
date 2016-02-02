import subprocess


# "eth0", "gsmtap.chan_type == 1", "-Tpdml", "-2", ">", "capture.xml"

def parse(filename, filter):
    subprocess.call(["tshark", "-i wlan0", "-R gsmtap.chan_type == 1", "-Tpdml", "-2"])
    return


# Capture BCCH framse
# subprocess.call(["tshark", "-r", "/home/nicolas/Bureau/capture-test1.pcap", "-i eth0", "-R gsmtap.chan_type == 1", "-Tpdml", "-2"])

# Capture CCCH frames
# subprocess.call(["tshark", "-r", "/home/nicolas/Bureau/capture-test1.pcap", "-i eth0", "-R gsmtap.chan_type == 2", "-Tpdml", "-2"])
# subprocess.call(["ls", "-l", "-a", "-h", "/home/nicolas/Bureau"])

# tshark -i eth0 -R "gsmtap.chan_type == 1" -Tpdml -2 > capture.xml

# subprocess.call('echo $HOME', shell=True)

# parameters
filename = "/home/nicolas/Bureau/capture-test1.pcap"
filter = "gsmtap.chan_type == 1"
parse(filename, filter)



