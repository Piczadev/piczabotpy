import sys
import os
import pytest
import pygame

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from entities.player import Player
from settings import *


def test_player_initialization():
    pygame.init()
    player = Player((100, 100))
    assert player.rect.topleft == (100, 100)
    assert player.speed == 8
    assert player.gravity == GRAVITY


def test_player_jump():
    pygame.init()
    player = Player((100, 100))
    initial_y_velocity = player.direction.y
    player.jump()
    assert player.direction.y == PLAYER_JUMP
    assert player.direction.y != initial_y_velocity
