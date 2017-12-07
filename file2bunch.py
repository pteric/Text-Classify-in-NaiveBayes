#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import cPickle as pickle 
from sklearn.datasets.base import Bunch
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

os.chdir("/Users/pengtuo/Downloads/corpus/")


def _readfile(path):
    with open(path, 'rb') as fp:
        content = fp.read()
    return content


def corpus2bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录，也就是分类信息
    if '.DS_Store' in catelist:
        catelist.remove('.DS_Store')
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)

    for cate in catelist:
        class_path = seg_path + cate + "/"
        file_list = os.listdir(class_path)
        if '.DS_Store' in file_list:
            file_list.remove('.DS_Store')
        for file_path in file_list:
            fullname = class_path + file_path
            bunch.label.append(cate)
            bunch.filenames.append(fullname)
            bunch.contents.append(_readfile(fullname))  # 读取文件内容

    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print "构建文本对象结束！！！"


if __name__ == "__main__":

    # 对训练集进行Bunch化操作：
    wordbag_path = "train/train_word_bag/train_set.dat"  # Bunch存储路径
    seg_path = "train/train_data_seg/"  # 卡方检验后分类语料库路径
    corpus2bunch(wordbag_path, seg_path)

    # 对测试集进行Bunch化操作：
    wordbag_path = "test/test_word_bag/test_set.dat"  # Bunch存储路径
    seg_path = "test/test_data_seg/"  # 分词后分类语料库路径
    # corpus2bunch(wordbag_path, seg_path)
