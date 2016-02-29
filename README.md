# BadIMSICore

## 1. Requirements 

The following dependencies need to be installed on the host before using BadIMSICore :
```
sudo apt-get install python-scipy tshark git 
```
BadIMSICore uses radio software dependencies such as:
- Gnuradio (https://github.com/gnuradio/gnuradio)
- libosmocore (https://github.com/osmocom/libosmocore)
- gr-gsm (https://github.com/ptrkrysik/gr-gsm)
- gr-osmosodr (https://github.com/osmocom/gr-osmosdr)
- uhd (https://github.com/EttusResearch/uhd)
- hackRF software (https://github.com/mossmann/hackrf)
- OpenBTS (https://github.com/RangeNetworks/openbts)

And also hardware dependencies:
- Ettus UHD | USRP B210 (https://www.ettus.com/product/details/UB210-KIT) used for the fake BTS.
- HackRF (https://greatscottgadgets.com/hackrf) used for the sniffing part.

## 2. Installation
To install BadIMSICore, just simply clone the git repository and launch the script deploy_core.sh to create system commands linked to the code :
```
git clone https://github.com/WarenUT/BadIMSICore 
cd ~/BadIMSICore
chmod +x deploy_core.sh
sudo ./deploy_core.sh
```
When the script is successfully launched, we have to following commands :
* badimsicore_listen
* badimsicore_openbts
* airprobe_rtlsdr_non_graphical
* badimsicore_sms_interceptor
* badimsicore_sms_sender
* badimsicore_tmsis

## 3. Usage 
For each command, you can display the required/optional arguments by the option -h

**badimsicore_listen**
This script uses the command 'airprobe_rtlsdr_non_graphical' which is a global script that listen to the GSM network and eventually record some GSM packets.  
```
sudo badimsicore_listen -h
usage: badimsicore_listen [-h] [-o {orange,sfr,bouygues_telecom}]
                          [-b {GSM-1900,GSM-850,TGSM-810,GSM-1800,GSM-750,EGSM-900,GSM-900,RGSM-900,GSM-450,GSM-480}]
                          [-t SCAN_TIME] [-n REPEAT] [-e]

optional arguments:
  -h, --help            show this help message and exit

listen:
  -o, --operator {orange,sfr,bouygues_telecom} search bts of this operator
  -b, --band {GSM-1900,GSM-850,TGSM-810,GSM-1800,GSM-750,EGSM-900,GSM-900,RGSM-900,GSM-450,GSM-480} search bts in this band of frequency
  -t, --scan_time SCAN_TIME   Set the scan time for each frequency
  -n, --repeat REPEAT         Set the number of repeat of the scanning cycle
  -e, --errors                list errors codes

```
i.e : I want to launch the sniffing to get all GSM-900 BTS from Orange Network Operator and repeat the sniffing 3 times :
```
sudo badimsicore_listen -o Orange -b GSM-900 -n 3
```

**badimsicore_openbts {start | stop}**
```
sudo badimsicore_openbts -h
usage: badimsicore_openbts [-h] {start,stop} ...

Usage of openbts

positional arguments:
  {start,stop}
    start       Start openbts
    stop        Stop openbts

optional arguments:
  -h, --help    show this help message and exit
  
sudo badimsicore_openbts start -h
usage: badimsicore_openbts start [-h] [-i CI] [-l LAC] [-n MNC] [-c MCC]
                                 [-m MESSAGE_REGISTRATION]
                                 [-p OPEN_REGISTRATION]

optional arguments:
  -h, --help            show this help message and exit
  -i, --ci CI        The Cell ID of the cell
  -l, --lac LAC     The LAC of the cell
  -n, --mnc MNC     The Mobile Network Code of the cell. Must have 2
                        digits
  -c, --mcc MCC     The Mobile Country Code of the cell. Must have 3
                        digits
  -m, --message-registration MESSAGE_REGISTRATION
                        The message upon registration of a mobile in the fake
                        network
  -p, --open-registration OPEN_REGISTRATION
                        The access authorization for the registration on the
                        fake network  
```
```
sudo badimsicore_openbts stop -h 
usage: badimsicore_openbts stop [-h]

optional arguments:
  -h, --help  show this help message and exit
```
To start the fake BTS with the following arguments :
- CI = 4534
- LAC = 45
- MNC = 01 (For Orange)
- MCC = 208 (France)
- The message registration = "Welcome to our network"
- OpenRegistration : open to everyone. (the correct syntax is '.*')

The right command would be:
```
sudo badimsicore_openbts start -i 4534 -l 45 -c 208 -n 01 -m "Welcome to our network" -p ".*"
```

**airprobe_rtlsdr_non_graphical**
```
sudo airprobe_rtlsdr_non_graphical -h
linux; GNU C++ version 4.8.4; Boost_105400; UHD_003.010.git-119-g42a3eeb6

usage: airprobe_rtlsdr_non_graphical [-h] [-g GAIN] [-p PPM] [-s SAMP_RATE]
                                     [-o SHIFTOFF]
                                     [-f FREQUENCIES [FREQUENCIES ...]]
                                     [-t SCAN_TIME] [-n REPEAT]

Configure sniffing parameters

optional arguments:
  -h, --help            show this help message and exit

grgsm arguments:
  -g, --gain GAIN  Set the amplification value
  -p, --ppm PPM     Set PPM Stream Modulation value
  -s, --samp_rate SAMP_RATE
                        Set the rate value of the antenna
  -o, --shiftoff SHIFTOFF
                        Set the shiftoff value
  -f, --frequencies FREQUENCIES [FREQUENCIES ...]
                        Set the list of frequencies to scan : 937000000
                        932950000 ...
  -t, --scan_time SCAN_TIME
                        Set the scan time for each frequency
  -n, --repeat REPEAT
                        Set the number of repeat of the scanning cycle
```
To use this script to listen on 937.7, 890 and 935.2 MHz, we launch it as :
``` 
airprobe_rtlsdr_non_graphical.py -f 937700000 890800000 935200000
``` 
See more documentation in the sniffing Wiki.


**badimsicore_sms_interceptor**
```
badimsicore_sms_interceptor -h
Usage: badimsicore_sms_interceptor -i <input>

Options:
  -h, --help            show this help message and exit
  -i INPUT, --input=INPUT
                        Log file to be analyzed
```
All the sms sent by the target are saved in the host's /var/log/syslog file.If we want to catch all the sms :
```
badimsicore_sms_interceptor -i /var/log/syslog 
```

**badimsicore_sms_sender**
```
badimsicore_sms_sender -h
Usage: badimsicore_sms_sender -r <recipient> -s <sender> -m <message>

Options:
  -h, --help            show this help message and exit
  -r RECIPIENT, --recipient=RECIPIENT
                        Recipient of the message
  -s SENDER, --sender=SENDER
                        Sender of the message
  -m MESSAGE, --message=MESSAGE
                        Message to be sent (160 chars max.)
```
To send a sms to the target mobile with the IMSI 208023944449510 with the source number : 0633449966, and the following message : "I love it" :
```
badimsicore_sms_sender -r 208023944449510 -s 0633449966 -m "I love it"
```

**badimsicore_tmsis**
Launch this command to get all tmsis connected to our fake bts.
```
badimsicore_tmsis
```

