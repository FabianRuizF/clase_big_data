from pyspark.sql import SparkSession




spark = SparkSession.builder.master('spark://139.144.62.82:7077').config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()

data = spark. #rellenar con las funciones faltantes
