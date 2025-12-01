import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        # Draw a glowing neon player (circle)
        pygame.draw.circle(self.image, settings.NEON_CYAN, (20, 20), 20)
        pygame.draw.circle(self.image, settings.WHITE, (20, 20), 15)  # Inner glow

        self.rect = self.image.get_rect(topleft=pos)

        # Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = settings.GRAVITY
        self.jump_speed = settings.PLAYER_JUMP

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.direction.y == 0:  # Simple jump check
            self.jump()

    def update(self, tiles):
        self.input()
        self.horizontal_collisions(tiles)
        self.vertical_collisions(tiles)
        self.apply_gravity()

    def horizontal_collisions(self, tiles):
        self.rect.x += self.direction.x * self.speed
        for tile in tiles:
            if tile.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = tile.rect.left
                elif self.direction.x < 0:
                    self.rect.left = tile.rect.right

    def vertical_collisions(self, tiles):
        self.apply_gravity()
        for tile in tiles:
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                elif self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.direction.y = 0

    def apply_gravity(self):
        self.direction.y += self.gravity

