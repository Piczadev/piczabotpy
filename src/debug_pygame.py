import pygame
import sys

print(f"Python version: {sys.version}")
print(f"Pygame version: {pygame.version.ver}")

try:
    pygame.init()
    print("pygame.init() successful")
except Exception as e:
    print(f"pygame.init() failed: {e}")

try:
    if not pygame.font:
        print("pygame.font module is None before explicit init")
    pygame.font.init()
    print(f"pygame.font.init() successful. Is initialized: {pygame.font.get_init()}")
    font = pygame.font.Font(None, 30)
    print("Successfully created Font object")
except Exception as e:
    print(f"pygame.font usage failed: {e}")
    import traceback
    traceback.print_exc()
