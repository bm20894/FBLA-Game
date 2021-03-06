import arcade

WIDTH = 800
HEIGHT = 600

scale = 0.4
dim = int(scale * 200)

mult = 50
margin = 100
coin_prob = 100
STARTSCORE = 500
COINSCORE = 10

from .player import Player
from .coin import FallingCoin, RisingCoin, BouncingCoin
from .data import data
from .question import questions
from .button import Button, check_press, check_release
from .worker import Worker
from .graph import graph
