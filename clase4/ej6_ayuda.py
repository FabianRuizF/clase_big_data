from pyspark.sql import SparkSession
import unicodedata as ud
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]




byte_to_use=1024*1024*0.5
part_num = 1660
spark = SparkSession.builder.master('spark://139.144.62.82:7077').appName('CalcDataFrame').config("spark.sql.files.minPartitionNum",part_num).config("spark.sql.files.maxPartitionBytes",  int(byte_to_use)).config("spark.default.parallelism", part_num).config("spark.driver.host",my_ip).config("spark.driver.memory", "2g").config("spark.executor.memory", "2g").getOrCreate()






data = spark.read.parquet("/mnt/nfs_share/data/central_west.parquet")
data.printSchema()

new_column_name_list=  [ud.normalize('NFKD',col).encode('ascii', errors='ignore').decode('utf-8') for col in data.columns]
new_column_name_list=  [col.replace("."," ") for col in new_column_name_list]
data = data.toDF(*new_column_name_list) 



data.printSchema()

list_of_numeric = []
for a in data.dtypes:
    print(a)
exprs = {x: "sum" for x in list_of_numeric }
print(exprs)
data.agg(exprs).show(vertical=True)