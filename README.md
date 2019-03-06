# FBLA-Game
Development of FBLA Computer Game and Simulation challenge

## Try it Out
So far, I have experimented with different types of sprite movement, physics, and levels.
* `sprite_movement.py` is a demonstration of keyboard input controlling sprite movement, in a different way than what is used in other examples. The control may or may not feel any smoother, it's kind of hard to tell.
* `coin_example.py` is a good example of using mouse input to control the movement of a sprite.
* `wall_example.py` shows a relationship between two sprites: the player and a wall. A "physics engine" is used to make sure the player can not move through the wall.
* `ball.py` is a simulation of a bouncing ball. No "physics engine" was used in this script, just variables storing values like Gravity Constants and the bounciness of the ball.
* `game.py` is the most complete program so far. It features multiple different levels, with some unique differences between them. There is also a "Game Over" screen after the player has collected all of the coins, with an option to play again.

## Installation
- *EXE*: Have a double-clickable file that runs the game with no terminal or dependancy installations
- *Pip*: Use a shell script for windows that installs the packagage from PYPI (pip install FBLA-Game)
	* Script could look something like this:

		#!/bin/bash
		pip install arcade FBLA-Game
		python3 -m FBLA-Game
