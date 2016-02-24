#!/bin/bash

coredir=/opt/BadIMSIBox/BadIMSICore
srcdir=$coredir/src
linkrootdir=/usr/local/sbin
linkdir=/usr/local/bin


function get(){
	git clone https://github.com/WarenUT/BadIMSICore.git -b master
}

function install(){
	sudo mkdir $coredir
	sudo cp -r ./BadIMSICore/src $coredir
	sudo cp -r ./BadIMSICore/resources $coredir
	
	sudo chmod u+x $srcdir/badimsicore_listen.py            $linkrootdir/badimsicore_listen
	sudo chmod u+x $srcdir/badimsicore_openbts.py           $linkrootdir/badimsicore_openbts
	sudo chmod a+x $srcdir/airprobe_rtlsdr_non_graphical.py $linkdir/airprobe_rtlsdr_non_graphical
	sudo chmod a+x $srcdir/badimsicore_sms_interceptor.py   $linkdir/badimsicore_sms_interceptor
	sudo chmod a+x $srcdir/badimsicore_sms_sender.py        $linkdir/badimsicore_sms_sender
	sudo chmod a+x $srcdir/badimsicore_tmsis.py             $linkdir/badimsicore_tmsis
	
	sudo ln -s $srcdir/badimsicore_listen.py            $linkrootdir/badimsicore_listen
	sudo ln -s $srcdir/badimsicore_openbts.py           $linkrootdir/badimsicore_openbts
	sudo ln -s $srcdir/airprobe_rtlsdr_non_graphical.py $linkdir/airprobe_rtlsdr_non_graphical
	sudo ln -s $srcdir/badimsicore_sms_interceptor.py   $linkdir/badimsicore_sms_interceptor
	sudo ln -s $srcdir/badimsicore_sms_sender.py        $linkdir/badimsicore_sms_sender
	sudo ln -s $srcdir/badimsicore_tmsis.py             $linkdir/badimsicore_tmsis
}

function clean(){
	sudo rm -rf $coredir
	sudo rm -rf $linkdir/badimsicore_*
	sudo rm -rf $linkrootdir/badimsicore_*
}

clean
get
install
