from document import *
from os import listdir
from os.path import isfile, join
from inverted_index import InvertedIndex

def exec():
    ii = InvertedIndex()
    for file in [f for f in listdir('../data') if isfile(join('../data', f))]:
        document_ = Document('../data/'+file)
        ii.add_document(document_)
    print(ii.db)
    ii.querry('a r e')

exec()
