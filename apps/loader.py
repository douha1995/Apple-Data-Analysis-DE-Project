import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql.functions import count
class Loader:
    def __init__(self):
        pass
    
    def load(self, df):
        pass
    

class NetFlixLoader(Loader):
    
    def load(self, path, df_filtered, df_movies, df_tv_shows, df_analytics):
        df_filtered.write.mode('overwrite').parquet(path)
        # Rating distribution
        df_analytics_pd = df_analytics.toPandas()
        df_analytics_pd.plot(kind = 'bar', x = 'rating', y = 'count', legend = False)
        plt.title('Distribution of Movies by Rating')
        plt.ylabel('Count')
        plt.xlabel('Rating')
        plt.tight_layout()
        plt.savefig('/opt/spark/data/netflix/transformed_data/movies_rating_distribution.png')
        
        # Category distribution
        category_count = pd.DataFrame(
            {
                'category': ['Movie', 'TV Show'],
                'count': [df_movies.count(), df_tv_shows.count()]
            }
        )
        category_count.plot(kind = 'bar', x = 'category', y = 'count', legend = False)
        plt.title('Entertainment Category Distribution')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('/opt/spark/data/netflix/transformed_data/category_distribution.png')
        
        # Genre Distribution
        genre_count = df_filtered.groupBy('listed_in').agg(count('*').alias('count')).orderBy('count', ascending=False)
        genre_count_pd = genre_count.limit(5).toPandas()
        
        plt.figure(figsize=(15,10))
        colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733']
        genre_count_pd.plot(kind = 'bar', x = 'listed_in', y = 'count', color = colors, legend = False)
        plt.title('Top 5 genre', pad=20)
        plt.ylabel('Count')
        plt.xlabel('Genre')
        plt.xticks(rotation = 45, ha = 'right')
        plt.tight_layout()
        plt.savefig('/opt/spark/data/netflix/transformed_data/genre_distribution.png')
        
        
        
        