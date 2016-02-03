#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sys

xmlfilename = sys.argv[1]
tree = ET.parse(xmlfilename)
space = ' '


for node in tree.iter('proto'):
    name = node.attrib.get('name')
    if name == "gsm_a.ccch":
        system_info_type = node.attrib.get('showname')
        print(system_info_type)
        for info in node.iter('field'):
            # case 3 and 4
            showname = info.attrib.get('showname')
            show = info.attrib.get('show')

            if "List of ARFCNs" in show:
                if info.attrib.get('show') is not None:
                    print(space,info.attrib.get('show'))

            if "Cell Identity - CI" in show:
                if info.attrib.get('show') is not None:
                    print(space,info.attrib.get('show'))

            if "Location Area Identification (LAI) -" in show:
                if info.attrib.get('showname') is not None:
                    print(space,info.attrib.get('showname'))

                for lac in info.iter('field'):
                    if lac.attrib.get('showname') is not None:
                        print(space, space,lac.attrib.get('showname'))
