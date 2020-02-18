#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 13/2/2020 11:03
 @Author:   balanceTan 
 @File:     convert_xml_to_txt.py
 @Software: PyCharm
 
"""
'''
1) the  xml of label file  is converted  .txt
2) be used to the str type of labels
'''
import os
import json
from cfg import *
import xml.etree.ElementTree as ET
import glob

with open(LABEL_TXT_FILE,'w') as f:
    for xml_File in glob.glob("{}/*xml".format(ANNOTATE_BASE_XML_DIR)):
        print(xml_File)
        tree = ET.parse(xml_File)
        _abs_Path = tree.findtext('path')
        abs_path, file_Name, = os.path.split(_abs_Path)
        w = tree.findtext('./size/width')
        h = tree.findtext('./size/height')
        w_scale, h_scale = int(w) / IMG_WIDTH, int(h) / IMG_HEIGHT
        f.write(file_Name)
        for item in tree.iter('item'):
            name = int(item.findtext('name'))

            xmin = int(item.findtext("bndbox/xmin"))
            ymin = int(item.findtext("bndbox/ymin"))
            xmax = int(item.findtext("bndbox/xmax"))
            ymax = int(item.findtext("bndbox/ymax"))
            _x1, _y1, _x2, _y2 = xmin, ymin, xmax, ymax
            _w, _h = _x2-_x1, _y2-_y1
            w_half, h_half = _w / 2, _h / 2
            _cx, _cy = _x1 + w_half, _y1 + h_half
            x1, y1, w, h = int(_cx / w_scale), int(_cy / h_scale), int(_w / w_scale), int(_h / h_scale)
            f.write(' {} {} {} {} {}'.format(int(name), x1, y1, w, h))
        f.write('\n')
