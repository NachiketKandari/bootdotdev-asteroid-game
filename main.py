import pygame
from constants import *
from player import *
from asteroid import *
from asteroidField import *
import sys
from shot import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Shot.containers = (updateable,drawable, shots)

    dt = 0 # delta time

    while True: # Loop for the screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            
            
        screen.fill("black")
        for a_drawable in drawable:
            a_drawable.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000 # milliseconds to seconds


if __name__ == "__main__":
    main()
