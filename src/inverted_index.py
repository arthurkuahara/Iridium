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

            querry_dict = dict(Counter(querry))

            for term in self.db:
                if term not in querry_dict:
                    querry_dict.update({term:0})


            term_set = set(self.db)

            norm_querry = 0
            norm_document = 0
            dot_product = 0

            print("{}{}".format('querry',querry_dict))
            for document in self.dl:
                norm_querry = 0
                norm_document = 0
                dot_product = 0 
                document_dict = dict()
                for term in term_set.union(set(querry)):
                    if term in self.db:
                        print(term)
                        # norm_querry += pow(W(querry_dict[term],len(self.db[term])),2)
                        # norm_document += pow(W(document_dict[term],len(self.db[term])),2)
                        # dot_product += W(querry_dict[term],len(self.db[term])) * W(document_dict[term],len(self.db[term]))
                    else:
                        norm_querry += pow(W(querry_dict[term],1),2)
                        norm_document += pow(W(document_dict[term],1),2)
                        dot_product += W(querry_dict[term],1) * W(document_dict[term],1)

                print(dot_product / (sqrt(norm_querry) * sqrt(norm_document)))
               
                print(document_dict)
                
            print(querry_dict)



