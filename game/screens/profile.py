import pygame

from constants import *

from screens.screen import Screen


class Profile(Screen):
    def __init__(
        self: object, win: pygame.Surface, assets_dir: str, framerate: int
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate: int = framerate

        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/full_background.png"
        )
        self.score: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/ScorePeq.png"
        )
        self.medalha: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/medalha.png"
        )
        self.profile_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 48
        )
        self.press_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 25
        )
        self.main_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 34
        )
        self.highscore_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 28
        )

    def run(self: object) -> int:
        running = True

        clock: pygame.time.Clock = pygame.time.Clock()
        while running:

            clock.tick(self.framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return QUIT
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        running = False

            if running:
                self.draw()

        return MAIN_MENU

    def draw(self: object) -> None:
        self.win.blit(self.background, (0, 0))

        rect_width: int = 560
        rect_height: int = 470
        rect_radius: int = 20
        rect_x: int = self.win.get_width() // 2 - rect_width // 2
        rect_y: int = 85
        rect_color: tuple = BLUE
        rect_alpha: int = 183

        self.draw_rounded_rect(
            self.win,
            rect_x,
            rect_y,
            rect_width,
            rect_height,
            rect_radius,
            rect_color,
            rect_alpha,
        )

        self.draw_highscore()
        self.draw_achievements()
        self.win.blit(self.profile_font.render("Profile", True, YELLOW), (240, 105))
        self.win.blit(self.main_font.render("Name:", True, WHITE), (170, 170))
        self.win.blit(
            self.press_font.render("Press space to menu... ", True, WHITE), (170, 510)
        )

        pygame.display.update()

    def draw_highscore(self: object) -> None:
        rect_x = 50
        rect_y = 225
        rect_width = 230
        rect_height = 270
        rect_thickness = 2  # Espessura do contorno
        pygame.draw.rect(
            self.win, WHITE, (rect_x, rect_y, rect_width, rect_height), rect_thickness
        )

        self.win.blit(self.score, (230, 232))
        self.win.blit(self.main_font.render("Highscore", True, YELLOW), (55, 240))
        self.win.blit(self.main_font.render("1.", True, WHITE), (75, 280))
        self.win.blit(self.main_font.render("2.", True, WHITE), (75, 320))
        self.win.blit(self.main_font.render("3.", True, WHITE), (75, 360))
        self.win.blit(self.main_font.render("4.", True, WHITE), (75, 400))
        self.win.blit(self.main_font.render("5.", True, WHITE), (75, 440))

    def draw_achievements(self: object) -> None:
        rect_x = 295
        rect_y = 225
        rect_width = 290
        rect_height = 270
        rect_thickness = 2  # Espessura do contorno
        pygame.draw.rect(
            self.win, WHITE, (rect_x, rect_y, rect_width, rect_height), rect_thickness
        )

        self.win.blit(self.medalha, (540, 235))
        self.win.blit(self.main_font.render("Achievements", True, YELLOW), (300, 240))
