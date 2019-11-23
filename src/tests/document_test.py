import sys
sys.path.insert(1,'../')
from document import *
import unittest



class DocumentTestCase(unittest.TestCase):
    def test_constructor(self):
        new_document = Document('./test_file')
        self.assertDictEqual(new_document.__dict__,{'id': './test_file', 'contents': ['hello','world']})

unittest.main()