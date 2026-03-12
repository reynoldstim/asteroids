import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main() -> None:
    pygame.init()
    game_clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # type: ignore[attr-defined]
    Asteroid.containers = (asteroids, updatable, drawable)
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField.containers = updatable  # type: ignore[attr-defined]
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
