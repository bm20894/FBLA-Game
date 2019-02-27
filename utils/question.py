"""
Question class
"""
import json, os
from . import mult

class Question:
    def __init__(self, text, value):
        self.text = text
        self.value = {k: v*mult for k, v in value.items()}

        # find answer
        vals = value.values()
        self.answer = list(value.keys())[list(vals).index(max(vals))]
        self.text += '\n\nAnswer: {}'.format(self.answer)

    def __repr__(self):
        msg = self.text[:20] + '...'
        return '<Question: \"{}\": ({}, {})>'.format(msg, self.value['yes'], self.value['no'])

file_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(file_path, 'question.json')) as f:
    data = json.load(f)

questions = [Question(**q) for q in data]
