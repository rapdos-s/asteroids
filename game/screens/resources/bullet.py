import math
import pygame

from constants import *


class Bullet:
    def __init__(
        self: object,
        player_x_position: int,
        player_y_position: int,
        angle: int,
    ) -> None:
        self.cosine: float = math.cos(math.radians(angle + 90))
        self.sine: float = math.sin(math.radians(angle + 90))

        self.x: int = player_x_position
        self.y: int = player_y_position

        self.dx: float = self.cosine * BULLET_SPEED
        self.dy: float = self.sine * BULLET_SPEED

        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, BULLET_SIZE, BULLET_SIZE)

    def move(self: object) -> None:
        self.x += self.dx
        self.y -= self.dy

    def draw(self: object, win: pygame.Surface) -> None:
        pygame.draw.rect(win, BULLET_COLOR, (self.x, self.y, BULLET_SIZE, BULLET_SIZE))

    def off_screen(self: object, win: pygame.Surface) -> bool:
        if self.x < 0 - BULLET_SIZE or self.x > win.get_width() + BULLET_SIZE:
            return True

        if self.y < 0 - BULLET_SIZE or self.y > win.get_height() + BULLET_SIZE:
            return True

        return False

    def update_bullet(self: object) -> None:
        self.rect = pygame.Rect(self.x, self.y, BULLET_SIZE, BULLET_SIZE)

    def get_collision(self: object) -> pygame.Rect:
        self.update_bullet()
        return self.rect
