#!/bin/bash

coredir=/opt/badimsibox/badimsicore
srcdir=$coredir/src
linkrootdir=/usr/local/sbin
linkdir=/usr/local/bin




function install(){
	sudo mkdir $coredir -p
	sudo cp -r ./src $coredir
	sudo cp -r ./resources $coredir
	
	sudo chmod 711 $srcdir/badimsicore_listen.py            $linkrootdir/badimsicore_listen
	sudo chmod 711 $srcdir/badimsicore_openbts.py           $linkrootdir/badimsicore_openbts
	sudo chmod 755 $srcdir/airprobe_rtlsdr_non_graphical.py $linkdir/airprobe_rtlsdr_non_graphical
	sudo chmod 755 $srcdir/badimsicore_sms_interceptor.py   $linkdir/badimsicore_sms_interceptor
	sudo chmod 755 $srcdir/badimsicore_sms_sender.py        $linkdir/badimsicore_sms_sender
	sudo chmod 755 $srcdir/badimsicore_tmsis.py             $linkdir/badimsicore_tmsis
	
	sudo ln -s $linkrootdir/badimsicore_listen $srcdir/badimsicore_listen.py
	sudo ln -s $linkrootdir/badimsicore_openbts $srcdir/badimsicore_openbts.py
	sudo ln -s $linkdir/airprobe_rtlsdr_non_graphical $srcdir/airprobe_rtlsdr_non_graphical.py
	sudo ln -s $linkdir/badimsicore_sms_interceptor $srcdir/badimsicore_sms_interceptor.py
	sudo ln -s $linkdir/badimsicore_sms_sender $srcdir/badimsicore_sms_sender.py
	sudo ln -s $linkdir/badimsicore_tmsis $srcdir/badimsicore_tmsis.py
}

function clean(){
	sudo rm -rf $coredir
	sudo rm -rf $linkdir/badimsicore_*
	sudo rm -rf $linkrootdir/badimsicore_*
}

clean
install
