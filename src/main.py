from document import *
from os import listdir
from os.path import isfile, join
from inverted_index import InvertedIndex
import sys  



def exec():
    #Querry comes from command line 
    querry_ = sys.argv[1:]
    ii = InvertedIndex()
    for file in [f for f in listdir('../data') if isfile(join('../data', f))]:
        document_ = Document('../data/'+file)
        ii.add_document(document_)
    sim_table = sorted(ii.querry(querry_))
    for document in sim_table:
        print(document)
exec()
