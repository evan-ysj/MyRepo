import engine_base
import re

class BOWInvertedIndexEngine(engine_base.SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
    
    def process_corpus(self, id, text):
        word_set = self.parse_text_to_words(text)
        for w in word_set:
            if w not in self.inverted_index:
                self.inverted_index[w] = []
            self.inverted_index[w].append(id)
    
    def search(self, query):
        result = []
        query_list = list(self.parse_text_to_words(query))
        query_to_id_index = list()
        for q in query_list:
            query_to_id_index.append(0)
            
        # If the inverted index of a query is none, return    
        for q in query_list:
            if q not in self.inverted_index:
                return result
        
        while True:
            # Aquire ids of all queries
            current_ids = []
            
            for idx, q in enumerate(query_list):
                current_index = query_to_id_index[idx]
                current_list = self.inverted_index[q]
                
                # Reach to the end of an inverted index list, end searching
                if current_index >= len(current_list):
                    return result
                
                current_ids.append(current_list[current_index])
            
            # If all the ids are same, it means that the query appears in all files; Add the file id into result
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_to_id_index = [x + 1 for x in query_to_id_index]
            # Otherwise increase the index of minimal id by one
            else:
                min_val = min(current_ids)
                min_val_index = current_ids.index(min_val)
                query_to_id_index[min_val_index] += 1
            
        return result
    
    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w ]', ' ', text)  # Remove all punctuations
        text = text.lower()                  # To lower case
        word_list = text.split(' ')          # Generate words list
        word_list = filter(None, word_list)  # Remove blank words
        return set(word_list)                # Return a set of words
    
    @staticmethod
    def query_match(query_set, words):       
        for q in query_set:
            if q not in words:
                return False
        return True

        
        
if __name__ == '__main__':
    search_engine = BOWInvertedIndexEngine()
    engine_base.main(search_engine)
    

