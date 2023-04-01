from pyspark.sql import SparkSession
from pyspark import SparkConf


spark = SparkSession.builder.master('spark://139.144.62.82:7077').getOrCreate()

from pyspark.mllib.random import RandomRDDs
data  = RandomRDDs.uniformVectorRDD(spark.sparkContext, 10000,6,6).map(lambda vector : vector.tolist()).toDF(["num1","num2","num3","num4","num5","num6"])
print(data.summary().show())
