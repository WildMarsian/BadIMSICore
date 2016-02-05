#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import bts
import sys, re


regex = re.compile(".*?\((.*?)\)")
btsList = []

if len(sys.argv) == 2:
    xmlfilename = sys.argv[1]
    tree = ET.parse(xmlfilename)
    space = ' '
    cpt = 1

    type1 = False
    type3 = False
    type4 = False

    arfcns = []

    for packet in tree.getroot():
        for proto in packet.iter('proto'):
            protoField = proto.attrib.get('name')
            if protoField == "gsm_a.ccch":
                for fieldGsm_a in proto.iter('field'):
                    fieldSystemType = fieldGsm_a.attrib.get('showname')
                    for fieldGsm_a_info in fieldGsm_a.iter('field'):
                        info = fieldGsm_a_info.attrib.get('show')
                        # For Type 1 packets
                        if (info is not None) and ("List of ARFCNs" in info):
                            arfcn = re.findall(r'\d+',info)
                            for a in arfcn:
                                arfcns.append(a)
                            type1 = True
                        # For Type 4 packets
                        if (info is not None) and ("Location Area Identification (LAI) - " in info):
                            tmp_lai = re.findall(r'\d+',info)
                            type4 = True

                        # For Type 3 packets
                        if (info is not None) and ("Cell Identity" in info):
                            cellId = regex.match(info)
                            type3 = True

            if (type1 == True) and (type3 == True) and (type4 == True):
                if(len(set(arfcns)) > 0):
                    btsObj = bts.BTS(tmp_lai[0],tmp_lai[1],tmp_lai[2],cellId.group(1),set(arfcns))
                    if btsObj not in btsList:
                        btsList.append(btsObj)
                    type1 = False
                    type3 = False
                    type4 = False
                    arfcns = []

        cpt = cpt + 1

    for eachBts in (btsList):
        print(eachBts)

else:
    print("You must put a xml file in args")
    print("badimsicore_sniffing_xml_parsing.py <xml-file>")
