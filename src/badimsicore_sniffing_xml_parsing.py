#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

"""
   This module performs the XML parsing in order
   to extract infos from the given captured file.
"""


import xml.etree.ElementTree as ET
import sys, re, os
import bts

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team"


regex = re.compile(".*?\((.*?)\)")


def usage():
    """
        Displays the error output message on stdout
    """
    print("You must put a xml file in args")
    print("badimsicore_sniffing_xml_parsing.py <xml-file>")

def is_valid_extension(filename, ext):
    """
        Check if the file has the good extension.
        :param filename: the file
        :param ext: an extension like '.xml'
        :return: boolean to verify if extension is correct
    """
    filename, extension = os.path.splitext(filename)
    return extension == ext

def parse_xml_file(xmlfilename):
    """
        :param xmlfilename: the xml file that contains all information on the sniffing
        :returns: a list that contains BTS Objects
    """
    btslist = {}
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
                if (len(arfcns) > 0):
                    btsObj = bts.BTS(tmp_lai[0], tmp_lai[1], tmp_lai[2], cellId.group(1), arfcns)
                    if btslist.get(cellId.group(1)) is None:
                        btslist[cellId.group(1)] = btsObj
                    else:
                        get_bts = btslist.get(cellId.group(1))
                        get_bts.add_arfcns(arfcns)

                    type1 = False
                    type3 = False
                    type4 = False
                    arfcns = []
    return btslist


def main():
    if len(sys.argv) == 2:
        xmlfilename = sys.argv[1]
        if is_valid_extension(xmlfilename, '.xml'):
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
