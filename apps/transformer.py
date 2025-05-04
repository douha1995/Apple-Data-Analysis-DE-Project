from pyspark.sql.window import Window
from pyspark.sql.functions import lead , col, window, desc, column, count

class Transformer:
    def __init__(self):
        pass
    
    def transform(self, input_df):
        pass
        

class NetFlixTransformer(Transformer):
    def transform(self, input_df):
        transformed_df = input_df.dropna(subset=['title', 'release_year', 'rating'])
        filtered_df = transformed_df.filter(col('release_year') >= 2005)
        movie_df = filtered_df.filter(col('type') == 'Movie')
        tv_show_df = filtered_df.filter(col('type') == 'TV Show')
        rating_count_df = filtered_df.groupBy('rating').agg(count('*').alias('count'))
        
        return filtered_df, movie_df, tv_show_df, rating_count_df
    