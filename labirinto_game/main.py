import pygame
import sys
from maze import generate_maze, draw_maze
from player import Player
from enemy import Enemy

# Inicializa o PyGame
pygame.init()

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Labirinto")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações do jogo
player = Player()
enemies = [Enemy() for _ in range(5)]

def game_loop():
    clock = pygame.time.Clock()
    maze = generate_maze()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_maze(screen, maze)
        player.update()
        player.draw(screen)
        
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
