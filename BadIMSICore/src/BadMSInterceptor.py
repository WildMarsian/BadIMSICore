from PyTail import PyTail

for line in PyTail("/var/log/syslog"):
    if "Decoded" in line:
        print(line)
