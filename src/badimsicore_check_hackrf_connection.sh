#/!bin/bash

# 1d50 is the hackrf vendor id
# 6089 is the hackrf product id
result=`sudo lsusb | grep "1d50:6089" | wc -l`
if [ $result -eq 0 ]
then
    exit 1
fi
exit 0
