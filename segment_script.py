#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import jieba.posseg as pseg
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 保存至文件
def _savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)


# 读取文件
def _readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


# 处理停用词
def process_stop_word(file_path):
    stop_words = _readfile(file_path).decode('gb18030')
    stop_words = stop_words.replace("\n", " ")
    stop_list = stop_words.split(" ")
    return stop_list


# 数据预处理
def corpus_segment(corpus_path, seg_path):

    # def判断该分词对是否符合内容
    def judeg_word(seg_pair):
        if seg_pair.flag == 'n':
            if len(seg_pair.word) > 1:
                if seg_pair.word not in stop_words_list:
                    return True
        return False
    
    cate_list = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录(即所有的类)

    # 获取每个目录（类别）下所有的子目录
    for cate in cate_list:
        seg_dir = seg_path + cate + "/"  # 拼出分词后存贮的对应目录路径如：train_corpus_seg/culture/
        if cate == '.DS_Store': continue
        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_dir)
            
        cate_dir = corpus_path + cate + '/'
        sub_list = os.listdir(cate_dir)

        # 获取每个子类别文件下的文件
        for sub_cate in sub_list:
            file_dir = corpus_path + cate + "/" + sub_cate # 拼出分类子目录的路径如：train_corpus/culure/cul2
            print '>>' * 25
            print 'Dealing in the direction named %s' % file_dir
            if os.path.isdir(file_dir):
                file_list = os.listdir(file_dir)
            else:
                continue

            for file_name in file_list:
                word_list = []
                fullname = file_dir + '/' + file_name
                content = _readfile(fullname)

                # 数据预处理
                content = content.replace("\r\n", "")  # 删除换行
                content = content.replace(" ", "")  # 删除空行、多余的空格
                regular = u'[^\u4E00-\u9FA5]'  # 非汉字
                content = content.decode("utf-8")
                content = re.sub(regular, '', content)
                seg_pairs = pseg.cut(content)  # 为文件内容分词
                for seg_pair in seg_pairs:
                    if judeg_word(seg_pair):
                        word_list.append(seg_pair.word)
                if len(word_list) >= 5:
                    print 'Writing content_seg file name %s' % file_name
                    _savefile(seg_dir + file_name, " ".join(word_list))  # 将处理后的文件保存到分词后语料目录
                    print 'DONE'
                    print '<<' * 25

    print "中文语料分词结束！！！"


if __name__ == "__main__":

    # 读取停用词
    stop_words_list = process_stop_word('/Users/pengtuo/Downloads/corpus/stop_words_ch.txt')

    # 对训练集进行分词
    corpus_path = "/Users/pengtuo/Downloads/corpus/train_data/"  # 未分词分类语料库路径
    seg_path = "/Users/pengtuo/Downloads/corpus/train_data_seg/"  # 分词后分类语料库路径
    # corpus_segment(corpus_path,seg_path)

    # 对测试集进行分词
    corpus_path = "/Users/pengtuo/Downloads/corpus/test_data/"  # 未分词分类语料库路径
    seg_path = "/Users/pengtuo/Downloads/corpus/test_data_seg/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)
