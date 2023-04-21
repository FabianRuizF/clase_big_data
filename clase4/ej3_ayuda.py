from pyspark.sql import SparkSession

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]



part_num = 80
spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('CalcDataFrame').config(###buscar nombre de config,part_num).config(###buscar nombre de config, part_num).config("spark.driver.host",my_ip).config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()
data = spark.read.parquet("/mnt/nfs_share/data/central_west.parquet")

data.printSchema()
print(data.count())
