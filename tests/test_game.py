import sys
import os
import pytest

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pygame
from settings import *


def test_pygame_import():
    """Verify pygame is installed and importable."""
    assert pygame.ver is not None


def test_settings_loaded():
    """Verify settings can be imported and have correct values."""
    assert SCREEN_WIDTH == 800
    assert SCREEN_HEIGHT == 600
    assert FPS == 60
    assert TITLE == "Liquid Glass Platformer"
