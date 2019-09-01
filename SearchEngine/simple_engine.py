import engine_base

class SimpleEngine(engine_base.SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_text = {}
    
    def process_corpus(self, id, text):
        self.__id_to_text[id] = text
    
    def search(self, query):
        result = []
        for id, text in self.__id_to_text.items():
            if query in text:
                result.append(id)
        return result

if __name__ == '__main__':
    search_engine = SimpleEngine()
    engine_base.main(search_engine)
    

