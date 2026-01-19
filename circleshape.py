from typing import Any

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: Any = None  # Will be set by subclasses at runtime

    def __init__(self, x: float, y: float, radius: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # type: ignore[arg-type]
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass
