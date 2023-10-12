"""Module with the function required by the task"""
import json


def callback_handler(word):
    """keyword_callback according the task"""
    return f'Found {word}'


def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    """Method for parsing json objects according the task"""
    output = []
    dictionary = json.loads(json_str)
    for key in dictionary:
        if key in required_fields:
            for keyword in keywords:
                if keyword in dictionary[key].split():
                    output.append(keyword_callback(keyword))

    return output
