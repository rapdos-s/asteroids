import pygame


class Asteroid:
    def __init__(
        self: object,
        size: int,
        x: int,
        y: int,
        assets_dir: str,
    ):
        self.x: int = x
        self.y: int = y
        self.assets_dir: str = assets_dir
        self.image: pygame.Surface = None
        self.points: int = 0
        self.width: int = self.image.get_width()
        self.height: int = self.image.get_height()
        self.rect: pygame.Rect = None

        if size == 1:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x1.png")
            self.points = 100
        elif size == 2:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x2.png")
            self.points = 50
        else:
            self.image = pygame.image.load(f"{self.assets_dir}/asteroid_x4.png")
            self.points = 20

        self.update_asteroid()

    def update_asteroid(self: object) -> None:
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self: object, win: pygame.Surface) -> None:
        win.blit(self.image, self.rect)
