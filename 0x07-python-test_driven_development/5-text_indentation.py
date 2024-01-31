#!/usr/bin/python3
"""text indentation"""

def text_indentation(text):
    """text indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    for char in characters:
        text = text.replace(char, char + '\n\n')
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    text = '\n'.join(lines)
    print(text)
