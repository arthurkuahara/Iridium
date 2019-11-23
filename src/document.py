import string

class Document:
    def __init__(self,path):
        self.id = path
        self.contents = self.open_file(path)

    def open_file(self,path):
        with open(path) as stream_reader:
            dirty_text = stream_reader.read()
            clean_text = dirty_text.translate(dirty_text.maketrans('','',string.punctuation))
            low_text = clean_text.lower()
            return low_text.split()

