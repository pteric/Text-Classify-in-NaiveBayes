#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

os.chdir('/Users/pengtuo/Downloads/corpus/')


# 读取文件
def _readfile(path):
    with open(path, 'rb') as fp:
        content = fp.read()
        content = content.decode('utf-8')
    return content


# 保存至文件
def _savefile(savepath, content_dict):
    with open(savepath, "wb") as fp:
        for key, value in content_dict.items():
            fp.write(key + ':' + str(value))
            fp.write('\n')


# 给该类构造一个方便统计的结构
def _contruct_word(cate_dir):
    cate_content = []
    file_list = os.listdir(cate_dir)
    for file_name in file_list:
        if file_name == '.DS_Store':
            continue
        file_path = cate_dir + '/' + file_name
        content = _readfile(file_path)
        content_tuple = set(content.split())
        cate_content.append(content_tuple)
    return cate_content


# 统计每个词在出现的该类别下的文档数
def count_word_frequents(seg_path, wordtimes_path):
    cate_list = os.listdir(seg_path)
    for cate in cate_list:
        if cate == '.DS_Store':
            continue
        word_frequents_dict = {}
        cate_dir = seg_path + cate
        save_file = wordtimes_path + cate + '_wordtimes.txt'
        cate_content = _contruct_word(cate_dir)
        for each_content in cate_content:
            for word in each_content:
                if len(word) >= 2:
                    word_frequents_dict[word] = word_frequents_dict.get(word, 0) + 1
        _savefile(save_file, word_frequents_dict)
        print '>>>' * 25
        print 'Writing in the file named %s \n' % save_file


if __name__ == '__main__':
    print('start')
    
    seg_path = 'train/train_data_seg/'     # 分词后训练集路径
    wordtimes_path = 'train/wordtimes/'    # 词频统计后存储位置
    count_word_frequents(seg_path, wordtimes_path)
