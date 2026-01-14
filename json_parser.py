from text_to_type import text_to_type

class JSONParser:
    def __init__(self, json):
        self.data = {}
        parse_object(json, self.data)
    
    def __str__(self):
        return "JSON Parser Object"
    
    def __repr__(self):
        return self.data

def parse_object(text, data):
    text = text.strip()
    # TODO: Implement
    pass