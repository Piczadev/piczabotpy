import pygame
from settings import GLASS_FILL, GLASS_BORDER


def create_glass_surface(width: int, height: int, radius: int = 20) -> pygame.Surface:
    """
    Creates a surface with a 'liquid glass' effect.
    """
    # Create a surface that supports alpha
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Draw the filled rounded rectangle (glass body)
    pygame.draw.rect(surface, GLASS_FILL, (0, 0, width, height), border_radius=radius)

    # Draw the border (glass edge)
    pygame.draw.rect(
        surface, GLASS_BORDER, (0, 0, width, height), width=2, border_radius=radius
    )

    return surface
