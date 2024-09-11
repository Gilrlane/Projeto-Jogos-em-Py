import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 30, 30)
        self.color = (0, 0, 255)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
