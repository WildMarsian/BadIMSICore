# BadIMSICore

## 1. Requirements 

The following dependencies need to be installed on the host before using BadIMSICore :
```
$ sudo apt-get install python-scipy tshark git 
```

BadIMSICore uses radio software dependencies such as:
- Gnuradio (https://github.com/gnuradio/gnuradio)
- OpenBTS (https://github.com/RangeNetworks/openbts)

And also hardware dependencies:
- Ettus UHD | USRP B210 (https://www.ettus.com/product/details/UB210-KIT)
- HackRF (https://greatscottgadgets.com/hackrf)

## 2. Installation
To install BadIMSICore, just simply clone the git repository and launch the script deploy_core.sh:
```
$ sudo git clone https://github.com/WarenUT/BadIMSICore 
$ cd ~/BadIMSICore
$ sudo deploy_core.sh
```
