from reader_factory import getDataSource
from transformer import  NetFlixTransformer
from extractor import NetFlixExtractor
from loader import NetFlixLoader

class Workflow:
    
    def __init__(self):
        pass
    

    def netflixPipeline(self):
            df = NetFlixExtractor().extract("csv", "/opt/spark/data/netflix/raw/netflix_titles.csv")
            # print(df.count())
            filtered_df, movie_df, tv_show_df, rating_count_df = NetFlixTransformer().transform(df)
            print(filtered_df.count())
            transformed_data_path = '/opt/spark/data/netflix/transformed_data/'
            
            NetFlixLoader().load(transformed_data_path, filtered_df, movie_df, tv_show_df,rating_count_df )
            
            print('ETL Process Ended Successfully!')
        
# workflow = Workflow().runner()

# workflow = Workflow().pipeline()
workflow = Workflow().netflixPipeline()
