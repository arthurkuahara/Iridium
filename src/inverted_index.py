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
                        
                for term in (term for term in self.db if term not in term_count):
                    self.db[term][document.id] = 0
                        
        def querry(self,q):
            # add querry to ii database
            doc_q = Querry(q)
            self.add_document(doc_q)
            
            explored = set()
            sim_table = dict()
            
            sum_w_doc    = 0
            sum_w_querry = 0
            dot_product  = 0
            
            n = len(self.dl)
            
            for doc in set(doc for doc in self.dl if doc not in explored):
               for term in self.db:
                   doc_product  += self.W(self.db[term][doc],n,len(self.db[term])) * self.W(self.db[term][doc_q.id],n,len[term])
                   sum_w_doc    += pow(self.db[term][doc],2)
                   sum_w_querry += pow(self.db[term][doc_q.id],2)
                sim = doc_product / (sqrt(sum_w_doc) * sqrt(sum_w_querry))
                sim_table[doc] = sim
                explored.add(doc)
            
            return sim_table
            
        @staticmethod
        def W(freq,n,nx):
            idf = log((n/nx),10)
            return freq * idf
        
        
            dirty_text = text
            clean_text = dirty_text.translate(dirty_text.maketrans('','',string.punctuation))
            ok_text = clean_text.lower()
            querry_dict = dict(Counter(ok_text))
            return querry_dict
            
            
       
                
                
                
