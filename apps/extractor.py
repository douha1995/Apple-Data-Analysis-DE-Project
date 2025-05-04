from reader_factory import getDataSource

class Extractor:
    def __init__(self):
        pass
    
    def extract(self, type, path):
        pass
      
    
class NetFlixExtractor(Extractor):
    def extract(self, source_type, source_path):
        
        df = getDataSource(
            data_type = source_type,
            path = source_path
        ).getDataframe()
        
        return df