import importlib

class FileParser:  
    def __init__(self, module_name):
        # Dynamically import the module
        self.parser = importlib.import_module(module_name)
    
    def parseHeader(self, file_name):
        header = self.parser.parse_header(file_name)
        return header