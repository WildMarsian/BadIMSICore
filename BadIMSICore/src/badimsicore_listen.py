import subprocess

class BadIMSICoreListener:

    @staticmethod
    def set_args(parser):
        group = parser.add_argument_group("listen")
        group.add_argument("-o", "--operator", help="search bts of this operator", default="orange", choices=["orange", "sfr", "bouygues_telecom"])
        group.add_argument("-t", "--scan-time", help="Set the scan time for each frequency", default=2, type=float)
        group.add_argument("-n", "--repeat", help="Set the number of repeat of the scanning cycle", default=1, type=int)

    @staticmethod
    def get_frequency(operator):



    @staticmethod
    def scan_frequencies(repeat, scan_time, frequencies):

        opts = ["python", "airprobe_rtlsdr_non_graphical.py"]
        opt_freq = ["-f"]
        opt_freq.extend(frequencies)
        opts.extend(opt_freq)
        opts.extend(["-t"], [5])
        opts.extend(["-n"], [2])
        subprocess.call(args=opts, shell=True)

    @staticmethod
    def toxml(xmlFile):
