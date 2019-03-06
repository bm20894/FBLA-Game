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

    def __repr__(self):
        msg = self.text[:20] + '...'
        return '<Question: {}>'.format(self.buttons)

questions = [Question(**q) for q in data]
