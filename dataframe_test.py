#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas
from math import log

df = pandas.DataFrame(index=['lady', 'tour', 'health'], columns=['a', 'b', 'c', 'd', 'e', 'f'])


df.loc['tour'] = {'a': 2, 'b': 10, 'c': 11, 'd': 18, 'e': 30}
df.loc['lady'] = {'a': 5, 'b': 3, 'c': 7, 'd': 10, 'e': 30}
df.loc['health'] = {'a': 8, 'b': 14, 'c': 3, 'd': 11, 'e': 30}


df = df.fillna(0)
print df

print type(df.loc['lady'])
print df.loc['lady']
print df.loc['lady'].as_matrix()
print type(df.loc['lady'].as_matrix())

print set(df.columns)

x_2 = set(['a', 'b', 'c', 'd', 'g'])
col = x_2 & set(df.columns)
print col

print df[list(col)]

p_ndarray = df[list(col)].as_matrix()
line_sum = map(sum, p_ndarray)  # numpy在行方向上求和
col_sum = map(sum, zip(*p_ndarray))  # numpy在列方向上求和
print line_sum
print col_sum
print max(line_sum), line_sum.index(max(line_sum))
print df.index[line_sum.index(max(line_sum))]


print list(df.loc[cate, col])
print type(df.loc[cate, col])
print sum(list(df.loc[cate, col]))

