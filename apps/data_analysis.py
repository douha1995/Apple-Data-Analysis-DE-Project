from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName('Apple_Analysis')\
    .getOrCreate()
    
df = spark.read.format('csv')\
    .option("header","True")\
    .load('/opt/spark/data/Transaction_updated.csv')
df.show()    