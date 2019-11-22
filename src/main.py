from document import *
from inverted_index import InvertedIndex

def exec():
    ii = InvertedIndex()
    new_doc = Querry("A B C")
    ii.add_document(new_doc)
    ii.querry('A')
    

exec()
