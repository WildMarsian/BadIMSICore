#!/bin/bash

coredir=/opt/badimsibox/badimsicore
srcdir=$coredir/src
linkrootdir=/usr/local/sbin
linkdir=/usr/local/bin
etcdir=/etc/badimsicore




function install(){
	sudo mkdir $coredir -p
	sudo mkdir $etcdir -p
	sudo cp -r ./src $coredir
	sudo cp -r ./resources/* $etcdir
	
	sudo chmod 711 $srcdir/badimsicore_listen.py
	sudo chmod 711 $srcdir/badimsicore_openbts.py
	sudo chmod 755 $srcdir/airprobe_rtlsdr_non_graphical.py
	sudo chmod 755 $srcdir/badimsicore_sms_interceptor.py
	sudo chmod 755 $srcdir/badimsicore_sms_sender.py
	sudo chmod 755 $srcdir/badimsicore_tmsis.py
	
	sudo ln -s $srcdir/badimsicore_listen.py $linkrootdir/badimsicore_listen
	sudo ln -s $srcdir/badimsicore_openbts.py $linkrootdir/badimsicore_openbts
	sudo ln -s $srcdir/airprobe_rtlsdr_non_graphical.py $linkdir/airprobe_rtlsdr_non_graphical
	sudo ln -s $srcdir/badimsicore_sms_interceptor.py $linkdir/badimsicore_sms_interceptor
	sudo ln -s $srcdir/badimsicore_sms_sender.py $linkdir/badimsicore_sms_sender
	sudo ln -s $srcdir/badimsicore_tmsis.py $linkdir/badimsicore_tmsis
}

function clean(){
	sudo rm -rf $coredir
	sudo rm $linkdir/badimsicore_*
	sudo rm $linkrootdir/badimsicore_*
	sudo rm $linkdir/airprobe_rtlsdr_non_graphical
}

clean
install
