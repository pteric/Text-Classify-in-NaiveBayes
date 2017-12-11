#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

os.chdir("/Users/pengtuo/Downloads/corpus/")


# 保存至文件
def _savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)


# 读取文件
def _readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
        content = content.decode('utf-8')
    return content


# 得到每个类别的文章数目
def count_cate_page(category):
    cate_page_num = {}
    for cate in category:
        cate_page_num[cate] = len(os.listdir('train/train_data_seg/' + cate))
    return cate_page_num


# 得到每个类别下，每个词在多少个文章中出现
def get_word_times(category):
    cate_word_times = dict()
    for cate in category:
        cate_word_times['dict_' + cate] = dict()
        with open('train/wordtimes/' + cate + '_wordtimes.txt', 'r') as df:
            for ele in [d.strip().split(':') for d in df]:
                cate_word_times['dict_'+cate][ele[0].decode('utf-8')] = ele[1]
    return cate_word_times


# 计算每个类里每个词的卡方值并且选取前N个记录入文件
def caculate_chi_write(category, cate_page_num, cate_word_times):
    for cate in category:
        dictname = cate_word_times['dict_'+cate]  # 将此类的词频词典赋予dictname
        chi_dic = {}  # 记录这个class中每个词的卡方检验值
        for kv in dictname:  # 遍历这个类别下的每个词，比较这个类别下每个词的CHI值
            kv_out_class = 0  # 统计一个新词时，初始化本类别外有这个词的文档数目为0  相当于b
            # not_kv_out_class = 0  # 统计一个新词时，初始化本类别外没有这个词的文档数目为0  相当于d
            kv_in_class = int(dictname[kv])   # 记录在这个分类下包含这个词的文档的数量  相当于a
            not_kv_in_class = (cate_page_num[cate]) - kv_in_class   # 记录在这个分类下不包含这个词的文档的数量  相当于c
            all_page_out_class = 0  # 初始化本类别外所有的文档数
            for cate_compare in category:
                if cate_compare != cate:
                    compare_name = cate_word_times['dict_'+cate_compare]
                    all_page_out_class += cate_page_num[cate_compare]
                    if kv in compare_name:
                        kv_out_class += int(compare_name[kv])

            not_kv_out_class = all_page_out_class - kv_out_class  # 本类所有别外没有用到这个词的文档数目  相当于d

            chi_dic[kv] = ((kv_in_class*not_kv_out_class - kv_out_class*not_kv_in_class) ** 2) / \
                          ((kv_in_class + kv_out_class) * (not_kv_in_class + not_kv_out_class))
            print kv, chi_dic[kv]

        # 按照chi值降序写入class_{cate}_chi_order.txt文件
        _savefile('train/train_chi_order/class_' + cate + '_chi_order.txt', '\n'.join(sorted(chi_dic, key=chi_dic.get, reverse=True)))
        N = 10000  # 只取CHI值较大的前1w个单词
        print("从 %s 类中选出 %d 个关键词" % (cate, N))
        chi_order = _readfile('train/train_chi_order/class_' + cate + '_chi_order.txt').split('\n')
        _savefile('train/train_chi_order/class_' + cate + '_chi_order_select.txt', '\n'.join(chi_order[0:N]))


if __name__ == '__main__':

    rootpath = "train/train_data_seg/"
    category = os.listdir(rootpath)
    if '.DS_Store' in category:
        category.remove('.DS_Store')

    cate_page_num = count_cate_page(category)

    cate_word_times = get_word_times(category)

    caculate_chi_write(category, cate_page_num, cate_word_times)

    print "CHI_run is finished!"
