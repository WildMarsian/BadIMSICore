#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import bts
import sys, re

regex = re.compile(".*?\((.*?)\)")
btsList = []

# adding a bitset


if len(sys.argv) == 2:
    xmlfilename = sys.argv[1]
    tree = ET.parse(xmlfilename)
    space = ' '
    cpt = 1

    for packet in tree.getroot():
        print("packet ",cpt)
        arfcns = []

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
                        # Type 3 and 4
                        if (info is not None) and ("Cell Identity" in info):
                            cellId = regex.match(info)
                            print("         Cell Identity:",cellId.group(1))
                        if (info is not None) and ("Location Area Identification (LAI) - " in info):
                            tmp_lai = re.findall(r'\d+',info)
                            print("      MCC:",tmp_lai[0],",MNC:",tmp_lai[1],",LAC:",tmp_lai[2])

                        # Type 1 and 2bis/2ter
                        if (info is not None) and ("List of ARFCNs" in info):
                            print("      ARFCNs: ",end="")
                            arfcn = re.findall(r'\d+',info)
                            for a in arfcn:
                                arfcns.append(a)
                            print(set(arfcns))

        cpt = cpt+1

else:
    print("You must put a xml file in args")
    print("badimsicore_sniffing_xml_parsing.py <xml-file>")