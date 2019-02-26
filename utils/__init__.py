import arcade

WIDTH = 800
HEIGHT = 600

scale = 0.4
dim = int(scale * 200)

from .coin import FallingCoin, RisingCoin, BouncingCoin
from .question import questions
from .button import YesButton, NoButton, check_press, check_release
from .worker import Worker
