import string

class Document:
    """This class represents a document as a 2-tuple of the text contents of the document and an id.
       path := string
    """
    def __init__(self,path):
        self.id = hex(hash(path))
        self.contents = self.open_file(path)

    def open_file(self,path):
        with open(path) as stream_reader:
            dirty_text = stream_reader.read()
            clean_text = dirty_text.translate(dirty_text.maketrans('','',string.punctuation))
            low_text = clean_text.lower()
            return low_text.split()
    
class Querry:
    
    def __init__(self,text):
        self.id = hex(hash(text))
        self.contents = self.format_text(text)
        
    def format_text(self,text):
        clean_text = text.translate(text.maketrans('','',string.punctuation))
        low_text = clean_text.lower()
        return low_text.split()
