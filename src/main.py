import pygame
import sys
from settings import *
from scenes.menu import Menu
from scenes.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game State
        self.state = 'menu' # menu, level
        self.menu = Menu(self.screen)
        self.level = Level(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            if self.state == 'menu':
                action = self.menu.handle_event(event)
                if action == 'start_game':
                    self.state = 'level'
            elif self.state == 'level':
                self.level.handle_event(event)

    def update(self):
        if self.state == 'menu':
            self.menu.update()
        elif self.state == 'level':
            self.level.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        if self.state == 'menu':
            self.menu.draw()
        elif self.state == 'level':
            self.level.draw()
            
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
