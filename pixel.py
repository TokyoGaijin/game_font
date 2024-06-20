import pygame

class Pixel:
    def __init__(self, x, y, color, size = 1):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)