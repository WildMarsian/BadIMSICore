#!/usr/bin/env python3.4
import subprocess




def main():
    opts = ['/home/badimsibox/BadIMSIBox/BadIMSICore/src/airprobe_rtlsdr_non_graphical.py', '-f', '937800000', '-t', '1', '-n', '10']
    subprocess.call(opts)


if __name__ == '__main__':
    main()
