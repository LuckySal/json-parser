from json_parser import parse_object

def text_to_type(text):
    text = text.strip()
    if not text:
        return ""
    if text == "true" or text == "false":
        return text
    if text == "null":
        return None
    if text[0] == "\"" and text[-1] == "\"":
        return text
    if text.isdigit():
        return int(text)
    if text.isdecimal():
        return float(text)
    if text[0] == "[" and text[-1] == "]":
        return text_to_list(text)
    if text[0] == "{" and text[-1] == "}":
        sub_dict = {}
        parse_object(text, sub_dict)
        return sub_dict
    raise ValueError("Unexpected string contents, cannot convert")

def text_to_list(text):
    text_list = []
    # TODO: Implement
    return text_list