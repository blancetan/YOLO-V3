#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 13/2/2020 9:10
 @Author:   balanceTan 
 @File:     convert_json_to_txt.py
 @Software: PyCharm
 
"""

'''
1) the  json of label file  is converted  .txt
2) be used to the int type of labels
'''

import os
import json
from cfg import *
import glob

with open(LABEL_TXT_FILE,'w') as f:
    for json_File in os.listdir(ANNOTATE_BASE_JSON_DIR):

        with open(os.path.join(ANNOTATE_BASE_JSON_DIR,json_File),'r') as jf:
            j = json.load(jf)
            print(j)
            img_Name = j['path'].split('\\')[-1]
            boxes = j['outputs']['object']
            print(boxes)
            wh = j['size']
            w, h = wh['width'], wh['height']

            w_scale, h_scale = w / IMG_WIDTH, h / IMG_HEIGHT

            f.write(img_Name)
            for box in boxes:
                bndbox = box['bndbox']
                _x1, _y1, _x2, _y2 = bndbox['xmin'], bndbox['ymin'], bndbox['xmax'], bndbox['ymax']
                _w, _h = _x2 - _x1, _y2 - _y1
                w_half, h_half = _w / 2, _h / 2
                _cx, _cy = _x1 + w_half, _y1 + h_half
                x1, y1, w, h = int(_cx / w_scale), int(_cy / h_scale), int(_w / w_scale), int(_h / h_scale)
                f.write(' {} {} {} {} {}'.format(int(box['name']), x1, y1, w, h))
        f.write('\n')




