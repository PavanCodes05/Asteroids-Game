import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2); 


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()

        player1.draw(screen)

        dt = clock.tick(60) // 1000
    

if __name__== "__main__":
    main()