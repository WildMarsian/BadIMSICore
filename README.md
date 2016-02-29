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
