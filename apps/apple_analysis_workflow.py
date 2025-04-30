from reader_factory import getDataSource
from transformer import AppleTransformer
class Workflow:
    
    def __init__(self):
        pass
    
    def runner(self):
        
        transaction_input_df = getDataSource(
            data_type = 'csv',
            path = '/opt/spark/data/Transaction_updated.csv'
            
        ).getDataframe()
        
        customer_input_df = getDataSource(
            data_type = 'csv',
            path = '/opt/spark/data/Customer_updated.csv'
        ).getDataframe()
        
        # Transaction data
        transaction_input_df.orderBy("customer_id", "transaction_date").show()
        
        input_df = {
            "trans_input_df" : transaction_input_df,
            "cust_input_df" : customer_input_df
        }
        
        # Customer who bought airpods after buying iphone
        AppleTransformer().transform(input_df)
        
        
        
workflow = Workflow().runner()
