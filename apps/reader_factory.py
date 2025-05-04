from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName('Apple_Analysis')\
    .getOrCreate()
    
spark.conf.set("spark.sql.shuffle.partitions", "5")
# Set Logging Level to WARN
spark.sparkContext.setLogLevel("ERROR")
    
    
class DataSource:
    """
    Abstract class
    """
    
    def __init__(self, path):
        self.path = path
        
    def getDataframe(self):
        """
        Abstract method, Function will be defined in the sub classes
        """
        
        raise ValueError("Not Implemented")
    
class CSVDataSource(DataSource):
    def getDataframe(self):
        
        return(
            spark.read.format("csv")\
                .option("header", "True")\
                .option("inferSchema", "true")\
                .load(self.path)
        )
        
class ParquetDataSource(DataSource):
    def getDataframe(self):
        
        return(
            spark.read.format("parquet")\
                .option("header", "True")\
                .load(self.path)
        )        

class ORCDataSource(DataSource):
    def getDataframe(self):
        
        return(
            spark.read.format("orc")\
                .option("header", "True")\
                .load(self.path)
        )
        
class DeltaDataSource(DataSource):
    def getDataframe(self):
        
        return(
            spark.read.format("delta")\
                .option("header", "True")\
                .load(self.path)
        )
        
def getDataSource(data_type, path):
    
    if data_type == "csv":
        return CSVDataSource(path)
    if data_type == "parquet":
        return ParquetDataSource(path)
    if data_type == "orc":
        return ORCDataSource(path)
    if data_type == "delta":
        return DeltaDataSource(path)
    else:
        raise ValueError(f"Not implemented for this file data type: {data_type}")
    