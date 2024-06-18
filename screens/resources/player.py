import math
import pygame

from screens.resources.bullet import Bullet

TURN_SPEED: int = 2
START_ANGLE: int = 0
MOVE_SPEED: int = 4


class Player:
    def __init__(
        self: object,
        x: int,
        y: int,
        display_width: int,
        display_height: int,
        assets_dir: str,
    ) -> None:
        self.assets_dir: str = assets_dir
        self.image: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/player_rocket.png"
        )

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

        self.player_cannon_x: int = 0
        self.player_cannon_y: int = 0
        self.bullets: list[Bullet] = []

        self.update_player()

    def check_movement(self: object):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move_forward()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.turn_left()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.turn_right()

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

    def shoot(self: object):
        self.player_cannon_x = self.x + (self.cosine / 2) * self.width / 2
        self.player_cannon_y = self.y - (self.sine / 2) * self.height / 2
        self.bullets.append(
            Bullet(self.player_cannon_x, self.player_cannon_y, self.angle)
        )
