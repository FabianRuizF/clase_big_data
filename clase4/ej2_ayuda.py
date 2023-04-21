from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

import socket

my_ip = ### completar aqui

spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('CalcDataFrame').config(###buscar nombre de configuracion).config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()

data = spark.read. #completar aqui
print(data.count())
