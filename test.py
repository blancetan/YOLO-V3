import torch
import numpy as np
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
