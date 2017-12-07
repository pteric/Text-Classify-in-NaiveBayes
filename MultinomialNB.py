#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from sklearn import metrics
import cPickle as pickle
from sklearn.naive_bayes import MultinomialNB

os.chdir("/Users/pengtuo/Downloads/corpus/")


# 读取bunch对象
def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


# 导入训练集
trainpath = "train/train_word_bag/train_tfdif_space.dat"
train_set = _readbunchobj(trainpath)

# 导入测试集
testpath = "test/test_word_bag/test_tfidf_space.dat"
test_set = _readbunchobj(testpath)

# 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

# 预测分类结果
predicted = clf.predict(test_set.tdm)
i = 0
for flabel, file_name, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        i += 1
        print file_name, ": 实际类别:", flabel, " -->预测类别:", expct_cate
print i
print "预测完毕!!!"


# 计算分类精度：
def metrics_result(actual, predict):
    print '精度:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted'))
    print '召回:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted'))
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted'))


metrics_result(test_set.label, predicted)
