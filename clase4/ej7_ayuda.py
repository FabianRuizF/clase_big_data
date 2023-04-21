from pyspark.sql import functions as f
from pyspark.sql import SparkSession
from pyspark import SparkConf

import unicodedata as ud
import socket


def find_outliers(df):

    # Identifying the numerical columns in a spark dataframe
    numeric_columns = [column[0] for column in df.dtypes if column[1]=='double'][:2]

    # Using the `for` loop to create new columns by identifying the outliers for each feature
    for column in numeric_columns:
        print(f"current column: {column}")
        less_Q1 = 'less_Q1_{}'.format(column)
        more_Q3 = 'more_Q3_{}'.format(column)
        Q1 = 'Q1_{}'.format(column)
        Q3 = 'Q3_{}'.format(column)

        # Q1 : First Quartile ., Q3 : Third Quartile
        Q1 = df.approxQuantile(column,[0.25],relativeError=0.05)
        Q3 = df.approxQuantile(column,[0.75],relativeError=0.05)
        
        # IQR : Inter Quantile Range
        # We need to define the index [0], as Q1 & Q3 are a set of lists., to perform a mathematical operation
        # Q1 & Q3 are defined seperately so as to have a clear indication on First Quantile & 3rd Quantile
        IQR = Q3[0] - Q1[0]
        
        #selecting the data, with -1.5*IQR to + 1.5*IQR., where param = 1.5 default value
        less_Q1 =  Q1[0] - 1.5*IQR
        more_Q3 =  Q3[0] + 1.5*IQR
        
        isOutlierCol = 'is_outlier_{}'.format(column)
        
        df = df.withColumn(isOutlierCol,f.when((df[column] > more_Q3) | (df[column] < less_Q1), 1).otherwise(0))
    

    # Selecting the specific columns which we have added above, to check if there are any outliers
    selected_columns = [column for column in df.columns if column.startswith("is_outlier")]

    # Adding all the outlier columns into a new colum "total_outliers", to see the total number of outliers
    df = df.withColumn('total_outliers',sum(df[column] for column in selected_columns))

    # Dropping the extra columns created above, just to create nice dataframe., without extra columns
    df = df.drop(*[column for column in df.columns if column.startswith("is_outlier")])

    return df

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
for x, t in data.dtypes:
    if(t=="double"):
        list_of_numeric.append(x)
exprs = {x: "sum" for x in list_of_numeric }
print(exprs)
data.agg(exprs).show(vertical=True)
exprs = {x: "mean" for x in list_of_numeric }
data.agg(exprs).show(vertical=True)


data =   find_outliers(data)
data = ##filtrar data aqui
print(f"current data count: {data.count()}")
