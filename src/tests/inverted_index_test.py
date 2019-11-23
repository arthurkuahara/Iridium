import sys
sys.path.insert(1,'../')
from inverted_index import InvertedIndex
from document import Document
import unittest


class InvertedIndexTestCase(unittest.TestCase):

    def test_constructor(self):
        new_index = InvertedIndex()
        self.assertDictEqual(new_index.__dict__,{'db':{},'dl':set()})

    def add_document(self):
        new_doc = Document('test_file')
        new_index = InvertedIndex()
        new_index.add_document(new_doc)
        self.assertIsInstance(new_index,InvertedIndex)

unittest.main()