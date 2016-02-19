#!/bin/bash

# Static variables
UHD_VENDOR_ID="2500"
BIND_FILE="/sys/bus/usb/drivers/usb/bind"
UNBIND_FILE="/sys/bus/usb/drivers/usb/unbind"

# Checking root rights
if [ "$EUID" -ne 0 ]
then 
    echo "Root rights needed"
    exit 1
fi

# Checking first parameter of the script (the idProduct of the device)
if [ -z "$1" ]
then
    echo "No UHD idProduct found, please specify one : "
    lsusb | grep $UHD_VENDOR_ID
    exit 2
fi

# Checking connection of the device to the system
found=$(lsusb -d $UHD_VENDOR_ID":"$1)
if [ -z "$found" ]
then
    critical_found=$(lsusb -d 0000:0000)
    if [ -z "$critical_found" ]
    then
        echo "Device probably failed"
        exit -2
    fi
    echo "Device not found, please reconnect the USB device"
    exit -1
fi

# Extracting Bus and Device number
bus=$( echo $found  | cut -d ' ' -f 2)
device=$(echo $found | cut -d ' ' -f 4 | cut -d ':' -f 1)

# Getting informations about the device
port_number=$(lsusb -D /dev/bus/usb/$bus/$device | grep bNumEndpoints | head -2 | tail -1 | awk '{print $2}')

# Store string used to control usb device
control_string=$port_number:$(($bus))

# Disable UHD
echo $control_string > $UNBIND_FILE

# Waiting a few seconds
sleep 2

# Enable UHD
echo $control_string > $BIND_FILE

exit 0

