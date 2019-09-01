import engine_base
import re

class BOWEngine(engine_base.SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_text = {}
    
    def process_corpus(self, id, text):
        self.__id_to_text[id] = self.parse_text_to_words(text)
    
    def search(self, query):
        result = []
        query_set = self.parse_text_to_words(query)
        for id, words in self.__id_to_text.items():
            if self.query_match(query_set, words):
                result.append(id)
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
    search_engine = BOWEngine()
    engine_base.main(search_engine)
    

