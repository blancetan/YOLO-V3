#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 13/2/2020 16:05
 @Author:   balanceTan 
 @File:     cluster.py
 @Software: PyCharm
 
"""
import glob
import xml.etree.ElementTree as ET
import numpy as np
from kmeans import kmeans, avg_iou

ANNOTATIONS_PATH = "./data/images_labeled"
CLUSTERS = 3


def load_dataset(path):
    dataset = []
    for xml_file in glob.glob("{}/*xml".format(path)):
        print(xml_file)
        tree = ET.parse(xml_file)

        height = int(tree.findtext("./size/height"))
        width = int(tree.findtext("./size/width"))
        # print('height:',height)
        # print('width',width)

        for item in tree.iter("item"):

            #  w,h 归一化
            # xmin = int(obj.findtext("bndbox/xmin")) / width
            # ymin = int(obj.findtext("bndbox/ymin")) / height
            # xmax = int(obj.findtext("bndbox/xmax")) / width
            # ymax = int(obj.findtext("bndbox/ymax")) / height

            xmin = int(item.findtext("bndbox/xmin"))
            ymin = int(item.findtext("bndbox/ymin"))
            xmax = int(item.findtext("bndbox/xmax"))
            ymax = int(item.findtext("bndbox/ymax"))

            # print('xmin:',xmin)
            # print('ymin:',ymin)
            # print('xmax:',xmax)
            # print('ymax:',ymax)

            xmin = np.float64(xmin)
            ymin = np.float64(ymin)
            xmax = np.float64(xmax)
            ymax = np.float64(ymax)

            if xmax == xmin or ymax == ymin:
                print(xml_file)
            dataset.append([xmax - xmin, ymax - ymin])
    return np.array(dataset)


if __name__ == '__main__':
    # print(__file__)
    for i in range(10000):
        data = load_dataset(ANNOTATIONS_PATH)
        print(data)
        print(data.shape)
        out = kmeans(data, k=CLUSTERS)
        # # clusters = [[10,13],[16,30],[33,23],[30,61],[62,45],[59,119],[116,90],[156,198],[373,326]]
        # # out= np.array(clusters)/416.0
        print(out)
    print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
    print("Boxes:\n {}-{}".format(out[:, 0] * 608, out[:, 1] * 608))
    ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
    print("Ratios:\n {}".format(sorted(ratios)))
