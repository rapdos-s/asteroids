import math
import pygame

TURN_SPEED: int = 3
START_ANGLE: int = 0
MOVE_SPEED: int = 10


class Player:
    def __init__(
        self: object,
        player_rocket: pygame.Surface,
        x: int,
        y: int,
        display_width: int,
        display_height: int,
    ) -> None:
        self.image: pygame.Surface = player_rocket

        self.is_alive: bool = True

        self.width: int = self.image.get_width()
        self.height: int = self.image.get_height()
        self.display_width: int = display_width
        self.display_height: int = display_height

        self.x: int = x
        self.y: int = y
        self.angle: int = START_ANGLE

        self.rotated_surface: pygame.Surface = None
        self.rotated_rect: pygame.Rect = None
        self.cosine: float = None
        self.sine: float = None

        self.update_player()

    def move_forward(self: object):
        self.x += self.cosine * MOVE_SPEED
        self.y -= self.sine * MOVE_SPEED
        self.check_location()
        self.update_player()

    def check_location(self: object):
        if self.x < 0 - self.width:
            self.x = self.display_width + self.width

        if self.x > self.display_width + self.width:
            self.x = 0 - self.width

        if self.y < 0 - self.height:
            self.y = self.display_height + self.height

        if self.y > self.display_height + self.height:
            self.y = 0 - self.height

    def turn_left(self: object):
        self.angle += TURN_SPEED
        self.update_player()

    def turn_right(self: object):
        self.angle -= TURN_SPEED
        self.update_player()

    def update_player(self: object) -> None:
        self.rotated_surface = pygame.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()

        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

    def draw(self: object, win: pygame.Surface) -> None:
        self.rotated_rect.center = (self.x, self.y)
        win.blit(self.rotated_surface, self.rotated_rect)

        self.rotated_rect.center = (
            self.x + self.display_width,
            self.y + self.display_height,
        )
        win.blit(self.rotated_surface, self.rotated_rect)

        self.rotated_rect.center = (self.x, self.y + self.display_height)
        win.blit(self.rotated_surface, self.rotated_rect)

        self.rotated_rect.center = (
            self.x + self.display_width,
            self.y + self.display_height,
        )
        win.blit(self.rotated_surface, self.rotated_rect)

    def alive(self: object) -> bool:
        return self.is_alive

    def kill(self: object) -> None:
        self.is_alive = False
