import engine_base
import re
import heapq

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BOWInvertedIndexEngine(engine_base.SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
    
    def process_corpus(self, id, text):
        word_set = self.parse_text_to_words(text)
        for w in word_set:
            if w not in self.inverted_index:
                self.inverted_index[w] = ListNode(id)
            else:
                __cur = self.inverted_index[w]
                while __cur.next:
                    __cur = __cur.next
                __cur.next = ListNode(id)
    
    def search(self, query):
        result = []
        query_list = list(self.parse_text_to_words(query))
            
        # If the inverted index of a query is none, return    
        for q in query_list:
            if q not in self.inverted_index:
                return result
        
        heap = []
        for q in query_list:
            heap.append((self.inverted_index[q].value, id(self.inverted_index[q]), self.inverted_index[q]))
        heapq.heapify(heap)
        
        key = ''
        count = 0
        while heap:
            pop = heapq.heappop(heap)
            if pop[0] != key:
                key = pop[0]
                count = 1
            else:
                count += 1
            if count == len(query_list):
                result.append(key)
            if pop[2].next:
                heapq.heappush(heap, (pop[2].next.value, id(pop[2].next), pop[2].next))
            
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
    

