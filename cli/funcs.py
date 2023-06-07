import os

def get_bytes(filepath:str)->int:
    '''Returns the number of bytes in filepath'''

    return os.path.getsize(filepath)

def get_words(filepath:str)->int:
    '''Returns the number of words in filepath'''

    with open(filepath, "r", encoding="utf8") as file:
        words = file.read().split()
        word_count = len(words)

    return word_count

def get_lines(filepath:str)->int:
    '''Returns the number of lines in filepath'''

    with open(filepath, "r", encoding = "utf8") as file:
        lines = file.readlines()
        line_count = len(lines)

    return line_count

def get_all(filepath:str)->tuple:
    '''Returns a tuple containing (line_count, word_count, byte_count) in filepath'''

    with open(filepath, "r", encoding="utf8") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

        file.seek(0)
        lines = file.readlines()
        line_count = len(lines)

    byte_count = get_bytes(filepath)
    return (line_count, word_count, byte_count)
