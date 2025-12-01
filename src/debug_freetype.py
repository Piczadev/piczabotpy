import pygame
import sys

try:
    import pygame.freetype
    print("Imported pygame.freetype successfully")
    pygame.init()
    font = pygame.freetype.SysFont(None, 24)
    print("Created freetype font")
    surf, rect = font.render("Test", (255, 255, 255))
    print("Rendered text")
except Exception as e:
    print(f"freetype failed: {e}")
    import traceback
    traceback.print_exc()
