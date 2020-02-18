#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 11/2/2020 9:23
 @Author:   balanceTan 
 @File:     cfg1.py
 @Software: PyCharm
"""

IMG_HEIGHT = 416
IMG_WIDTH = 416

CLASS_NUM = 10

LABEL_FILE = './data/label.txt'
ANNOTATE_BASE_JSON_DIR = './data/images_annotated/json'
ANNOTATE_BASE_XML_DIR = './data/images_annotated/xml'

ANCHORS_GROUP = {
    13: [[51, 22], [52, 22], [53, 22]],
    26: [[54, 22], [55, 22], [56, 22]],
    52: [[57, 22], [58, 22], [59, 22]],
}
ANCHORS_GROUP_AREA = {
    13: [x*y for x,y in ANCHORS_GROUP[13]],
    26: [x*y for x,y in ANCHORS_GROUP[26]],
    52: [x*y for x,y in ANCHORS_GROUP[52]],
}

# print(ANCHORS_GROUP_AREA)