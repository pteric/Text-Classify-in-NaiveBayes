#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from sklearn.datasets.base import Bunch
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer

os.chdir("/Users/pengtuo/Downloads/corpus/")


def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch


def _writebunchobj(path, bunchobj):
    with open(path, "wb") as file_obj:
        pickle.dump(bunchobj, file_obj)


def vector_space(bunch_path, space_path, train_tfidf_path=None):
    bunch = _readbunchobj(bunch_path)
    tfidf_space = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[], vocabulary={})

    if train_tfidf_path is None:
        train_vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
        train_tdm = train_vectorizer.fit_transform(bunch.contents)
        print "the shape of train is "+repr(train_tdm.shape)
        tfidf_space.tdm = train_tdm
        tfidf_space.vocabulary = train_vectorizer.vocabulary_

    else:
        trainbunch = _readbunchobj(train_tfidf_path)
        test_vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, vocabulary=trainbunch.vocabulary)
        test_tdm = test_vectorizer.fit_transform(bunch.contents)
        print "the shape of train is " + repr(test_tdm.shape)
        tfidf_space.tdm = test_tdm
        tfidf_space.vocabulary = trainbunch.vocabulary

    _writebunchobj(space_path, tfidf_space)
    print "if-idf词向量空间实例创建成功！！！"


if __name__ == '__main__':

    bunch_path = "train/train_word_bag/train_set.dat"
    space_path = "train/train_word_bag/train_tfdif_space.dat"
    vector_space(bunch_path, space_path)

    train_tfidf_path = "train/train_word_bag/train_tfdif_space.dat"
    bunch_path = "test/test_word_bag/test_set.dat"
    space_path = "test/test_word_bag/test_tfidf_space.dat"
    vector_space(bunch_path, space_path, train_tfidf_path)
