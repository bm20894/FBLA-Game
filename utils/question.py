"""
Question class
"""
import json, os
from . import data, mult

class Question:
    def __init__(self, text, buttons):
        self.text = text
        self.buttons = {k: b*mult for k, b in buttons.items()}

        # find answer
        vals = buttons.values()
        self.answer = list(buttons.keys())[list(vals).index(max(vals))]
        self.text += '\n\nAnswer: {}'.format(self.answer)

    def __repr__(self):
        msg = self.text[:20] + '...'
        return '<Question: {}>'.format(self.buttons)

# file_path = os.path.dirname(os.path.abspath(__file__))
# with open(os.path.join(file_path, 'question.json')) as f:
    # data = json.load(f)

questions = [Question(**q) for q in data]
