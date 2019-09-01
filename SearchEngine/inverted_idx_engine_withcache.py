import engine_base
import inverted_index_engine
import pylru

class LRUCache(object):
    def __init__(self, size = 32):
        self.cache = pylru.lrucache(size)
    
    def has(self, key):
        return key in self.cache
    
    def get(self, key):
        return self.cache[key]
    
    def set(self, key, value):
        self.cache[key] = value

class BOWInvertedIndexEngineWithCache(inverted_index_engine.BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('Cache hit!')
            return self.get(query)
        
        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)
            
        return result


        
        
if __name__ == '__main__':
    search_engine = BOWInvertedIndexEngineWithCache()
    engine_base.main(search_engine)
    

