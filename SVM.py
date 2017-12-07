#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from sklearn import metrics
from sklearn.svm import SVC
import cPickle as pickle

os.chdir("/Users/pengtuo/Downloads/corpus/")


# 读取bunch对象
def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


# 导入训练集
trainpath = "train/train_word_bag/train_set.dat"
train_set = _readbunchobj(trainpath)

# 导入测试集
testpath = "test/test_word_bag/test_set.dat"
test_set = _readbunchobj(testpath)

# 训练分类器：输入词袋向量和分类标签
clf = SVC(kernel='linear').fit(train_set.tdm, train_set.label)

predicted = clf.predict(test_set.tdm)


# 计算分类精度：
def metrics_result(actual, predict):
    print '精度:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted'))
    print '召回:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted'))
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted'))


metrics_result(test_set.label, predicted)
