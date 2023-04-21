from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]

spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('CalcDataFrame').config("spark.driver.host",my_ip).config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()


data = spark.read.parquet("/mnt/nfs_share/data/central_west.parquet")
print(data.count())
