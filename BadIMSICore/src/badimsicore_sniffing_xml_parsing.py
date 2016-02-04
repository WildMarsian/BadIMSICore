#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys
import re

regex = re.compile(".*?\((.*?)\)")

network_operators = {'01':'Orange', '02':'Orange', '09':'SFR', '10':'SFR', '11':'SFR', '15':'Free', '16':'Free', '20':'Bouygues Telecom', '21':'Bouygues Telecom' }
'''
codes = network_operators.keys()
for code in codes:
    print(network_operators[code])
'''

# adding a bitset

if len(sys.argv) == 2:
    xmlfilename = sys.argv[1]
    tree = ET.parse(xmlfilename)
    space = ' '
    cpt = 1

    for packet in tree.getroot():
        print("packet ",cpt)

        for proto in packet.iter('proto'):
            protoField = proto.attrib.get('name')
            if protoField == "gsmtap":
                print(" gsmtap")
                for fieldGsmtap in proto.iter('field'):
                    fieldName = fieldGsmtap.attrib.get('name')
                    if "gsmtap.snr_db" in fieldName:
                        if fieldName is not None:
                            ratio = re.findall(r'\d+',fieldGsmtap.attrib.get('showname'))
                            print("     Noise:", ratio[0])

            if protoField == "gsm_a.ccch":
                print(" gsm_a.ccch")

                for fieldGsm_a in proto.iter('field'):
                    fieldSystemType = fieldGsm_a.attrib.get('showname')
                    if fieldSystemType is not None and (("System Information Type" in fieldSystemType)):
                        print("     ",fieldSystemType)

                    for fieldGsm_a_info in fieldGsm_a.iter('field'):
                        info = fieldGsm_a_info.attrib.get('show')
                        if (info is not None) and ("Location Area Identification (LAI) - " in info):
                            tmp_lai = re.findall(r'\d+',info)
                            print("      MCC:",tmp_lai[0],",MNC:",tmp_lai[1],",LAC:",tmp_lai[2])

                        if (info is not None) and ("List of ARFCNs" in info):
                            print("      ARFCNs: ",end="")
                            arfcns = re.findall(r'\d+',info)
                            for a in arfcns:
                                print("     ",a,end="")
                        if (info is not None) and ("Cell Identity" in info):
                            cellId = regex.match(info)
                            print("         Cell Identity:",cellId.group(1))

        cpt = cpt+1

else:
    print("You must put a xml file in args")
    print("badimsicore_sniffing_xml_parsing.py <xml-file>")