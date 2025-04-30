from pyspark.sql.window import Window
from pyspark.sql.functions import lead , col

class Transformer:
    def __init__(self):
        pass
    
    def transform(self, input_df):
        pass
        
class AppleTransformer(Transformer):
    """
        Customers who have bought airpods after buying iphone.
    """
    def transform(self, input_df):
        
        transaction_input_df = input_df.get("trans_input_df")
        
        customer_input_df = input_df.get('cust_input_df')
        
        
        transaction_input_df.show()
        
        window_product = Window.partitionBy("customer_id").orderBy("transaction_date")
        lead_product = transaction_input_df.withColumn(
            "next_product_name" , lead("product_name").over(window_product)     
        )
        
        lead_product.orderBy("customer_id","transaction_date","product_name").show()
        
        filtered_product = lead_product.filter((col("product_name") == "iPhone") & (col("next_product_name") == "AirPods" ))
        filtered_product.orderBy("customer_id","transaction_date","product_name").show()
        
        
        # Customer data
        customer_input_df.show()
        
        cust_trans_df = filtered_product.join(
            customer_input_df,
            'customer_id'
        )
        
        # Transaction which customers do 
        cust_trans_df.select(
            "customer_id",
            "customer_name",
            "location",
            "product_name"
        ).show()
        
        return cust_trans_df.select(
            "customer_id",
            "customer_name",
            "location",
            "product_name"
        )