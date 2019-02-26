"""
Question class
"""
import json, os

class Question:
    mult = 5000
    def __init__(self, text, value):
        self.text = text
        self.value = {k: v*self.mult for k, v in value.items()}
    def __repr__(self):
        msg = self.text[:20] + '...'
        return '<Question: \"{}\": ({}, {})>'.format(msg, self.value['yes'], self.value['no'])

file_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(file_path, 'question.json')) as f:
    data = json.load(f)

questions = [Question(**q) for q in data]
