from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, HiveContext, Row
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.mllib.feature import Word2Vec

#Pull in data here were each sentence is a row, split by word, average all sentences in article to get vector for article, and make average vector for input, calculate cosine similarity between input vector and article vector 

word2vec = Word2Vec()
model = word2vec.fit(inp)
