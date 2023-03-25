from pyspark.sql import SparkSession


spark = SparkSession.builder.master('spark://139.144.62.82:7077').getOrCreate()
