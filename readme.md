# 新闻文本分类 -- 自实现朴素贝叶斯分类器

本项目利用100万的新闻文本，利用[朴素贝叶斯](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)来进行文本分类，新闻包括[car、culture、energy、entertainment、finance、health、house、IT、military、sport]十个类，每个类10w条新闻，并且其中，50万数据用以训练，50万数据用以测试

## 项目文件包括：
- `dataframe_test.py`：一个`pandas.dataframe`的用法测试文件；
- `get_data_format.py`：用以分析[搜狗实验室新闻语料](http://www.sogou.com/labs/resource/cs.php)，将其中混合的新闻分出多个类（但是这个语料库的新闻质量不高且不均匀，我用八爪鱼自行爬取了100W）
- `segment_script.py`：数据预处理，用来将原新闻预料分词，其中主要利用了[jieba](https://github.com/fxsjy/jieba)分词，分词的要求为：
    - 只取汉字
    - 去掉停用词
    - 只取名词
    - 去掉单个字
- `class_word_frequents.py`：统计每个词在其类别下被包含的文档数，用以卡方检验计算；
- `chisquare_test.py`：卡方检验，筛选出每个类下卡方值高的特征词，卡方检验的原理与理解推荐此文---[特征选择算法之开方检验](http://www.blogjava.net/zhenandaci/archive/2008/08/31/225966.html)；
- `file2bunch.py`：分别将所有训练文件与测试文件的文件名、内容与对应类读入`Bunch`数据结构，并将其序列化存储到一个文件，方便后面程序的读写与计算；
- `construct_tfidfspace.py`：创建训练数据的tfidf矩阵，并且利用训练数据的词袋创建测试数据的tfidf矩阵，将测试数据与训练数据放在同一词向量空间里；
- `MultinomialNB.py`：利用`sklearn`中的多项式朴素贝叶斯分类器，以tfidf为参数进行预测；
- `bim_bayes.py`：自编二项式朴素贝叶斯分类器，其中利用`laplas`平滑算法进行零概率处理，利用`pandas`与`numpy`加速50万数据的训练与测试，经过多次测试，平均训练时间为10min，平均测试时间为23min，平均总体正确率、召回率和F测度都为`84%`；

