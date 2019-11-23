from document import *
from inverted_index import InvertedIndex

def exec():
    
    ii = InvertedIndex()
    test_doc = Document("../data/abc")
    test_doc2 = Document("../data/a") 
    ii.add_document(test_doc)
    ii.add_document(test_doc2)
    print(ii.db)
    ii.querry('r')

    

exec()
