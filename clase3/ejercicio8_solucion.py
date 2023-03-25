from pyspark.sql import SparkSession
from pyspark import SparkConf



spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('CalcDataFrame').config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()

from pyspark.mllib.random import RandomRDDs
data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, 10000,6,100).map(lambda vector : vector.tolist()).toDF()
print(data.summary().show())
