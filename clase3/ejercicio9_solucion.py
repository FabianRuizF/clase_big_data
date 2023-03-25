from pyspark.sql import SparkSession
from pyspark import SparkConf



spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('Calc_Big_DataFrame').config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()

from pyspark.mllib.linalg import DenseVector
from pyspark.mllib.random import RandomRDDs
data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, 100000000,6,100).map(lambda a : a.tolist()).toDF()

exprs = {x: "sum" for x in data.columns }
print(exprs)
data.agg(exprs).show()
