from pyspark.sql import SparkSession
from pyspark import SparkConf


spark = SparkSession.builder.master('spark://139.144.62.82:7077').getOrCreate()

from pyspark.mllib.linalg import DenseVector
from pyspark.mllib.random import RandomRDDs
data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, 10000,6,6).sum()
