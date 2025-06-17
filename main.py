import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot


def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    #initalization code
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = updatable, drawable, asteroids
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                exit(0)
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
                    break
                
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0











if __name__ ==  "__main__":
    main()
