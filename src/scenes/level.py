import pygame
from settings import *
from entities.player import Player
from utils.glass import create_glass_surface

class Level:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        
        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        # Setup
        self.setup_level()

    def setup_level(self):
        # Player
        self.player = Player((100, SCREEN_HEIGHT - 150))
        self.all_sprites.add(self.player)
        
        # Platforms (Glass style)
        self.create_platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40) # Floor
        self.create_platform(200, 400, 200, 20)
        self.create_platform(500, 300, 200, 20)
        self.create_platform(100, 200, 150, 20)

    def create_platform(self, x, y, width, height):
        platform = pygame.sprite.Sprite()
        platform.image = create_glass_surface(width, height, radius=10)
        platform.rect = platform.image.get_rect(topleft=(x, y))
        self.all_sprites.add(platform)
        self.collision_sprites.add(platform)

    def handle_event(self, event):
        pass

    def update(self):
        self.player.update(self.collision_sprites)

    def draw(self):
        self.all_sprites.draw(self.display_surface)
