import math
import pygame
import random

from constants import *


class Asteroid:
    def __init__(
        self: object,
        win: pygame.Surface,
        assets_dir: str,
    ):
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir

        self.size: int = random.choice([1, 2, 4])
        self.image: pygame.Surface = None
        self.points: int = 0
        self.rect: pygame.Rect = None
        self.destroyed: bool = False

        if self.size == ASTEROID_SMALL:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x1.png")
            self.points = 100
        elif self.size == ASTEROID_MEDIUM:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x2.png")
            self.points = 50
        else:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x4.png")
            self.points = 20

        self.width: int = self.image.get_width()
        self.height: int = self.image.get_height()

        self.x: int = 0
        self.y: int = 0
        self.set_initial_position()

        self.direction: int = 0
        self.set_direction()

        self.speed: int = random.randint(1, 3)
        self.step: int = 0

        self.update_asteroid()

    def set_initial_position(self: object) -> None:
        positions: list[Tuple(int, int)] = [
            (-self.width, random.randint(0, self.win.get_height())),
            (
                self.win.get_width() + self.width,
                random.randint(0, self.win.get_height()),
            ),
            (
                random.randint(0, self.win.get_width()),
                -self.height,
            ),
            (
                random.randint(0, self.win.get_width()),
                self.win.get_height() + self.height,
            ),
        ]

        self.x, self.y = random.choice(positions)

    def set_direction(self: object) -> None:
        if self.x < 0:
            self.direction_x = random.randint(1, 3)
        elif self.x > self.win.get_width():
            self.direction_x = random.randint(-3, -1)
        else:
            self.direction_x = random.choice([-3, -2, 2, 3])

        if self.y < 0:
            self.direction_y = random.randint(1, 3)
        elif self.y > self.win.get_height():
            self.direction_y = random.randint(-3, -1)
        else:
            self.direction_y = random.choice([-3, -2, 2, 3])

    def update_asteroid(self: object) -> None:
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self: object, win: pygame.Surface) -> None:
        win.blit(self.image, self.rect)

    def is_destroyed(self: object) -> bool:
        return self.destroyed
    
    def get_size() -> int:
        return self.size

    def move(self: object) -> None:
        self.step += 1
        if self.step % self.speed == 0:
            self.x += self.direction_x
            self.y += self.direction_y
            self.update_asteroid()
            self.step = 0

    def off_screen(self: object, win: pygame.Surface) -> bool:
        if self.x < 0 - self.width or self.x > win.get_width() + self.width:
            return True

        if self.y < 0 - self.height or self.y > win.get_height() + self.height:
            return True

        return False
