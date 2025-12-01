import pygame
from settings import *
from utils.glass import create_glass_surface

class Menu:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 30)
        
        # Login / Start Box
        self.box_width = 400
        self.box_height = 300
        self.box_x = (SCREEN_WIDTH - self.box_width) // 2
        self.box_y = (SCREEN_HEIGHT - self.box_height) // 2
        
        self.glass_panel = create_glass_surface(self.box_width, self.box_height)
        self.glass_rect = self.glass_panel.get_rect(topleft=(self.box_x, self.box_y))
        
        # Text
        self.title_surf = self.font.render("LOGIN", True, NEON_CYAN)
        self.title_rect = self.title_surf.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + 50))
        
        self.prompt_surf = self.small_font.render("Press ENTER to Start", True, WHITE)
        self.prompt_rect = self.prompt_surf.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + 150))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'start_game'
        return None

    def update(self):
        pass

    def draw(self):
        # Draw Glass Panel
        self.display_surface.blit(self.glass_panel, self.glass_rect)
        
        # Draw Text
        self.display_surface.blit(self.title_surf, self.title_rect)
        self.display_surface.blit(self.prompt_surf, self.prompt_rect)
