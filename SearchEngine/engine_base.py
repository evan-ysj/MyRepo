class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus is not implemented')
    
    def search(self, query):
        raise Exception('search is not implemented')
    
def main(search_engine):
    for path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(path)
    
    while True:
        query = input('input query:')
        result = search_engine.search(query)
        print('Found {} result(s):'.format(len(result)))
        for r in result:
            print(r)
