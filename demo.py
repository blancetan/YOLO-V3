#!/usr/bin/python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 10/2/2020 16:33
 @Author:   balanceTan 
 @File:     demo.py.py
 @Software: PyCharm
"""

import numpy as np
import torch
import math


# x, y = math.modf(32/3)
# print(x)
# print(y)

# a = [2, 3, 4, 5]
# b = [1, 5, 9, *a]
#
# print(b)

# def one_hot(cls_num, v):
#     b = np.zeros(cls_num)
#     b[v] = 1.
#     return b
# print(one_hot(10,2))
a = torch.Tensor([1, 2, 3, 4])
b = a < 3  # mask
print(b)
print(a[b])
print(b.nonzero())
print(a[b.nonzero()])

# a = torch.Tensor([[1, 2], [5, 6], [3, 1], [2, 8]])
# # b = a < 3
# # print(b)
# # print(a[b])
# b = a[:, 1] > 5
# print(b)
# print(a[b])
# print(b.nonzero())

# a = np.array([1, 2, 5, 7, 10, 29, 39])
# print(a)
# LABEL_FILE_PATH = "data/person_label.txt"
# with open(LABEL_FILE_PATH) as f:
#     data = f.readlines()
#     line = data[0]
#     strs = line.split()
#     print(strs[0])
    # print(data[0].split())
    # print(data[0])
    # print(data[0].strip())
#     for line in f:
#         # print(line,end='')
#         print(line,end='')
#         print(type(line))

# def one_hot(cls_num, v):
#
#     b = np.zeros(cls_num)
#     b[v] = 1.
#     return b
# data = one_hot(10,1)
# print(data)


# print(int(0.3))
# print(int(0.5))
# print(int(0.6))
# print(int(0.8))
# print(int(1.2))

# ANCHORS_GROUP = {
#     13: [[51, 22], [52, 22], [53, 22]],
#     26: [[54, 22], [55, 22], [56, 22]],
#     52: [[57, 22], [58, 22], [59, 22]]
# }

# for feature_size,anchors in ANCHORS_GROUP.items():
# #     print('feature_size',feature_size)
# #     print('anchors',anchors)
# # name_dic = {'name':'tanxiangli'}
# # print(name_dic)
# # print(name_dic.items())
#
# # for key,value in {'name':'tanxiangli'}:
#     # print('key',key)
#     # print('value',value)

# flag_list = [1, 2, 3, ]
#
# print(flag_list)
# print(len(flag_list))
# print(flag_list[-1])
# print(flag_list.pop())
# print(flag_list)
# import copy
# a = 40
# b = copy.copy(a)
# print(a)
# print(b)
# a = 50
# b = copy.copy(a)
# print(a)
# print(b)
# import os
# import json
# IMAGES_BASE_DIR = r'C:\Users\18145844\Desktop\images\outputs'
#
# for jsonFile in os.listdir(IMAGES_BASE_DIR):
#     print(jsonFile)
#     with open(os.path.join(IMAGES_BASE_DIR,jsonFile)) as f:
#         datas = f.readlines()
#         print(type(datas))
#         print(datas[0])
#         print(type(datas[0]))
#         data_dic = json.loads(datas[0])
#         data_dic.
#         print(type(data_dic))
#         print(data_dic)
#         data_dic.

# dict1={'a':'e','b':'f','c':'g'}
#
# with open('tt.txt', 'w') as f:
#     f.write(str(dict1))
#
# with open('tt.txt','r') as f:
#     read1=f.read()
#     print(read1)
#     print(type(read1))
#
# with open('tt.txt','r') as f:
#     read2=eval(f.read())
#     print(read2)
#     print(type(read2))
import numpy as np

# print('使用列表生成一维数组')
# x = [1, 2, 3, 4, 5]
# print(x)
# print(type(x))
# data = np.array(x)
# print(type(data))
# print(data)
#
#
# print('使用列表生成二维数组')
# x =[[1, 2], [3, 4], [5, 6]]
# print(x)
# print(type(x))
# data = np.array(x)
# print(data)
# print(type(data))
# print(data.ndim)
# print(data.dtype)
# print(data.shape)
# print(data.size)
#
#
# x = np.zeros((2, 3), dtype=np.int8)
# print(x)
#
# x = np.ones((3, 4), dtype=np.int8)
# print(x)
#
# x = np.zeros((2, 3))
# print(x)
# print(x.dtype)
#
#
# x = np.empty((4, 5), dtype=np.float32)
# print(x)
#
# x = np.ones((3, 4))
# print(x)
#
# x = np.empty((4, 5), dtype=np.float32)
# print(x)
#
# print("使用arange生成连续的元素")
# x = np.arange(6)
# print(x)
# x = np.arange(6).reshape(2, 3)
# y = x.astype(dtype=np.float64)
# print(y)
# print(x)
# x = np.arange(1, 6, 2)
# print(x)
#
#
# print('使用astype复制数组，并转换元素类型')
# x = np.arange(6).reshape(2, 3)
# print(x)
# y = x.astype(dtype=np.float64)
# print(y)
#
# print('将字符串元素转为数值元素')
# x = np.array(['1', '2', '3', '4'])
# y = x.astype(dtype=np.int8)
# print(x)
# print(y)
#
# print("使用其它的数组的数据类型作为参数")
# x = np.array([1, 2, 3, 4, 5],dtype=np.float64)
# print(x)
# y = np.arange(3, dtype=np.int32)
# print(y)
# print(y.astype(x.dtype))
#
#
# print('ndarray数组和标量及数组间运算')
# x = np.array([[1, 2, 3],[4, 5, 6]])
# y = np.array([[2, 3, 4],[5, 6, 7]])
# print(x * 2)
# print(x > 2)
# print(x + y)
# print(x * y)
# print(x > y)
#
#
# print('ndarray的基本索引') #索引降维度
# x = np.array([[1, 2], [3, 4], [5, 6]])
# print(x)
# print(x[0])
# print(x[0][1])
# print(x[0, 1])
# x = np.array([[[1, 2],[3, 4]],[[5, 6], [7, 8]]])
# print(x[0])
# print(x[0][1])
# print(x[0][1][0])
# print(x[0, 1])
# print(x[0, 1, 0])
#
# y = x[0].copy()  #生成一个副本
# z = x[0]    # 没有生成副本
# print(y)
# print(y[0,0])
# y[0,0] = 9
# z[0,0] = 10
# print(y)
# print(x)
# print(z)
# print(x)
#
#
# print('ndarray切片') #切片不会降维度
# x = np.array([1, 2, 3, 4, 5])
# print(x[1:3])
# print(x[ :3])
# print(x[1:])
# print(x[:])
# print(x[:5:2])
#
# x = np.array([[1, 2], [3, 4],[5, 6]])
# print(x[:2])
# print(x[:2, :1])
# print(x[:2, 1])
# x[:2,:1] = 0
# print(x)
# x[:2,:1] = [[9],[8]]
# print(x)
#
# x = np.arange(24).reshape(2,3,4)
# print(x)
# print(x[:1,:1,:1])
# print(x[:2,:1,:1])
# print(x[:2,0,0][0])
#
#
# print('ndarray布尔型索引') #if index is True  result is value
# x = np.array([1,2,3,4])
# y = np.array([True, True, False, True])
# print(x[y])
# print(x[y==False])
# print(x > 3)
# print(x[x > 3])


# print("ndarray的花式索引：使用整形数组作为索引")
# x = np.array([1,2,3,4,5,6])
# print(x[[0,1,2]])
# print(x[[-1,-2,-3]])
# x = np.array([[1,2],[3,4],[5,6]])
# print(x[0,1])
# print(x[[0,1],[0,1]])
# print(x[[0,1]][:,[0,1]])

# x = np.arange(24).reshape(4,3,2)
# print(x)
# print(x[[0,1,2,3],[1],[1]])

# print("ndarray数组的转置和轴对称")
# k = np.arange(12).reshape((3,4))
# print(k)
# #转置
# print(k.T)
# #内积（点乘）
# print(np.dot(k,k.T))
# #高维数组的轴对象
# k = np.arange(24).reshape(2,3,4)
# print(k)
# print(k.shape)
# print(k[0][1][2])
# print(k[0,1,2])
# #轴变换
# k = k.transpose(1,0,2)
# print(k.shape)
# #轴变换做转置
# x = np.arange(6).reshape(2,3)
# print(x)
# x = x.transpose(1,0)
# print(x)
# #轴交换
# x = x.swapaxes(0,1)
# print(x)


# print("numpy的基本统计方法")
# x = np.array([[1,2],[3,4],[5,6]])
# print(x.shape)
# print(x.mean())
# print(x.mean(axis=1))
# print(x.mean(axis=0))
# print(x.sum())
# print(x.sum(axis=1))
# print(x.max())
# print(x.max(axis=1))
# print(x.max(axis=0))

print(".sort就地排序")
x = np.array([[6,1,3],[1,5,2]])
x.sort(axis=1)
print(x)

# print("ndarray的存取")
# x = np.array([[1,6,2],[6,1,3],[1,5,2]])
# print(x)
# np.save("file",x) #以二进制.npy保存
# y = np.load("file.npy")
# print(y)
#
# print("矩阵求逆")
# x = np.array([[1,1],[1,2]])
# print(x)
# y = np.linalg.inv(x)
# print(y)
# print(x.dot(y))
#
# print("numpy中的随机数")
# x = np.random.randint(0,2,size=100000) #模拟抛硬币
# print((x>0).sum())#正面的次数
#截断正态分布  正态分布  均匀分布
#
#
# print("where函数的使用")
# cond = np.array([True,False,False,False])
# x = np.where(cond,-2,2)
# print(x)
# cond = np.array([1,2,3,4])
# x = np.where(cond>2,-2,2)
# print(x)

#boradcast 原则（提升数组维度，满足运算要求）：
# 1. 数组维度不同，后缘维度的轴长相同
# 2. 数组维度相同，其中有个轴长度为1,另外轴的长度要相同