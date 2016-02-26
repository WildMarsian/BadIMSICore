#!/bin/bash

boxrootdir=/opt/badimsibox
coredir=$boxrootdir/badimsicore
srcdir=$coredir/src
linkrootdir=/usr/local/sbin
linkdir=/usr/local/bin




function install(){
	sudo mkdir $coredir -p
	sudo cp -r ./src $coredir
	sudo cp -r ./resources $coredir
	sudo chmod 755 -R $boxrootdir

	sudo chmod 711 $srcdir/badimsicore_listen.py
	sudo chmod 711 $srcdir/badimsicore_openbts.py
	sudo chmod 711 $srcdir/badimsicore_reload_usb_usrp.sh
	sudo chmod 755 $srcdir/badimsicore_check_hackrf_connection.sh
	sudo chmod 755 $srcdir/airprobe_rtlsdr_non_graphical.py
	sudo chmod 755 $srcdir/badimsicore_sms_interceptor.py
	sudo chmod 755 $srcdir/badimsicore_sms_sender.py
	sudo chmod 755 $srcdir/badimsicore_tmsis.py
	
	sudo ln -s $srcdir/badimsicore_listen.py                  $linkrootdir/badimsicore_listen
	sudo ln -s $srcdir/badimsicore_openbts.py                 $linkrootdir/badimsicore_openbts
	sudo ln -s $srcdir/badimsicore_reload_usb_usrp.sh         $linkrootdir/badimsicore_reload_usb_usrp
	sudo ln -s $srcdir/badimsicore_check_hackrf_connection.py $linkdir/badimsicore_check_hackrf_connection
	sudo ln -s $srcdir/airprobe_rtlsdr_non_graphical.py       $linkdir/airprobe_rtlsdr_non_graphical
	sudo ln -s $srcdir/badimsicore_sms_interceptor.py         $linkdir/badimsicore_sms_interceptor
	sudo ln -s $srcdir/badimsicore_sms_sender.py              $linkdir/badimsicore_sms_sender
	sudo ln -s $srcdir/badimsicore_tmsis.py                   $linkdir/badimsicore_tmsis
}

function clean(){
	sudo rm -rf $coredir
	sudo rm $linkdir/badimsicore_*
	sudo rm $linkrootdir/badimsicore_*
	sudo rm $linkdir/airprobe_rtlsdr_non_graphical
}

clean
install
