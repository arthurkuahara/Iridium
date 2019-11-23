from collections import Counter
from math import log, pow, sqrt
import string
from document import *
from random import choice

class InvertedIndex:

        def __init__(self):
                self.db = dict()
                self.dl = set()

        def add_document(self,document):
                self.dl.add(document.id)
                term_count = dict(Counter(document.contents))
                
                for term in term_count:
                    if term in self.db:
                        self.db[term][document.id] = term_count[term]
                    else:
                        self.db[term]  = {document.id:term_count[term]}
                        
              
                        
        def querry(self,querry):
            def W(tf,nx):
                    idf = log(len(self.dl)/nx,10)
                    return idf * tf

            clean_querry = [term for term in querry if term in self.db]
            querry_dict = dict(Counter(clean_querry))
            for term in self.db:
                if term not in querry_dict:
                    querry_dict.update({term:0})
            norm_querry = sqrt(
                    sum(
                        (pow(W(querry_dict[term],len(self.db[term])),2) for term in querry_dict)
                        ))
            
            for document in self.dl:
                document_dict = dict()
                for term in self.db:
                    if document in self.db[term]:
                        document_dict.update({term:self.db[term][document]})
                    else:
                        document_dict.update({term:0})
                norm_document = sqrt(
                    sum(
                        (pow(W(document_dict[term],len(self.db[term])),2) for term in document_dict)
                        ))
                dot_product = sum(
                    ( (W(document_dict[term],len(self.db[term])) * W(querry_dict[term],len(self.db[term])) ) for term in self.db )
                )
                print("{} {} {} {}".format(document_dict,norm_querry,norm_document,dot_product))


            
                
            



