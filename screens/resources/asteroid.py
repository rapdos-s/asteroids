import math
import pygame
import random

from constants import *


class Asteroid:
    def __init__(
        self: object,
        win: pygame.Surface,
        assets_dir: str,
        size: int,
        x: int = 0,
        y: int = 0,
    ):
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir

        self.size: int = size
        self.image: pygame.Surface = None
        self.points: int = 0
        self.destroyed: bool = False

        if self.size == ASTEROID_SMALL_SIZE:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x1.png")
            self.points = ASTEROID_SMALL_POINTS
        elif self.size == ASTEROID_MEDIUM_SIZE:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x2.png")
            self.points = ASTEROID_MEDIUM_POINTS
        else:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x4.png")
            self.points = ASTEROID_BIG_POINTS

        self.rect = self.image.get_rect()
        self.width: int = self.image.get_width()
        self.height: int = self.image.get_height()

        self.x: int = x
        self.y: int = y
        if self.x == 0 and self.y == 0:
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
        self.rect.center = (self.x, self.y)

    def draw(self: object, win: pygame.Surface) -> None:
        win.blit(self.image, self.rect)

    def draw_collision(self: object, win: pygame.Surface) -> None:
        collision: pygame.Rect = self.get_collision()
        pygame.draw.rect(win, (0, 255, 0), collision, 2)

    def is_destroyed(self: object) -> bool:
        return self.destroyed

    def get_size(self: object) -> int:
        return self.size

    def get_collision(self: object) -> pygame.Rect:
        collision: pygame.Rect = pygame.Rect(
            self.x,
            self.y,
            self.width * ASTEROID_COLLISION_REDUCER,
            self.height * ASTEROID_COLLISION_REDUCER,
        )
        collision.center = (self.x, self.y)
        return collision

    def get_points(self: object) -> int:
        return self.points

    def get_x(self: object) -> int:
        return self.x

    def get_y(self: object) -> int:
        return self.y

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
