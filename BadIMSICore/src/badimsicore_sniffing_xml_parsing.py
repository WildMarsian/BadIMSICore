#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import bts
import sys, re, os

"""
    This script takes an xml file and parse it. It returns a list of BTS.
"""


regex = re.compile(".*?\((.*?)\)")
"""
    BTS list
"""
btsList = []

def usage():
    """
        The error output message on stdout
    """
    print("You must put a xml file in args")
    print("badimsicore_sniffing_xml_parsing.py <xml-file>")

def is_valid_extension(filename, ext):
    """
    :param filename: the file
    :param ext: an extension like '.xml'
    :return: boolean to verify if extension is correct
    """
    filename, extension = os.path.splitext(filename)
    return extension == ext

def parse_xml_file(xmlfilename):
    """
    :param xmlfilename: the xml file that contains all information on the sniffing
    :return: a list that contains BTS Objects
    """
    tree = ET.parse(xmlfilename)
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
                            arfcn = re.findall(r'\d+', info)
                            for a in (arfcn):
                                arfcns.append(a)
                            type1 = True
                        # For Type 4 packets
                        if (info is not None) and ("Location Area Identification (LAI) - " in info):
                            tmp_lai = re.findall(r'\d+', info)
                            type4 = True

                        # For Type 3 packets
                        if (info is not None) and ("Cell Identity" in info):
                            cellId = regex.match(info)
                            type3 = True

            if (type1 == True) and (type3 == True) and (type4 == True):
                if (len(set(arfcns)) > 0):
                    btsObj = bts.BTS(tmp_lai[0], tmp_lai[1], tmp_lai[2], cellId.group(1), set(arfcns))
                    if btsObj not in btsList:
                        btsList.append(btsObj)
                    type1 = False
                    type3 = False
                    type4 = False
                    arfcns = []
    return btsList

def main():
    if len(sys.argv) == 2:

        xmlfilename = sys.argv[1]
        if is_valid_extension(xmlfilename,'.xml'):
            list_bts = parse_xml_file(xmlfilename)
            for b in list_bts:
                print(b)
        else:
            print("The extension of your file must be in xml")
            sys.exit(2)

    else:
        usage()

if __name__ == '__main__':
    main()
