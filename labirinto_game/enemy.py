import pygame
import random

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, 770), random.randint(0, 570), 30, 30)
        self.color = (255, 0, 0)
    
    def update(self):
        # Lógica de movimento dos inimigos
        pass
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
