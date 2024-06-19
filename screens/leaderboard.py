import pygame

from constants import *

from screens.screen import Screen


class Leaderboard(Screen):
    def __init__(
        self: object,
        win: pygame.Surface,
        assets_dir: str,
        framerate: int,
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate: int = framerate

        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/full_background.png"
        )
        self.score: pygame.Surface = pygame.image.load(f"{self.assets_dir}/Score.png")
        self.leaderboard_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 48
        )
        self.highscore_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 23
        )
        self.main_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 34
        )
        self.press_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 27
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
                        return MAIN_MENU
                    if event.key == pygame.K_SPACE:
                        running = False
            if running:
                self.draw()

        return MAIN_MENU

    def draw(self: object) -> None:
        self.win.blit(self.background, (0, 0))

        rect_width: int = 495
        rect_height: int = 435
        rect_radius: int = 20
        rect_x: int = self.win.get_width() // 2 - rect_width // 2
        rect_y: int = 68
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

        self.win.blit(self.score, (265, 75))
        self.win.blit(
            self.leaderboard_font.render("Leaderboard", True, YELLOW), (165, 175)
        )
        self.win.blit(self.highscore_font.render("Highscore", True, YELLOW), (255, 220))
        self.win.blit(
            self.main_font.render("KIM:   2089   DATA: 04/03", True, WHITE), (80, 250)
        )
        self.win.blit(
            self.main_font.render("CAIO:   1850  DATA: 04/03", True, WHITE), (80, 290)
        )
        self.win.blit(
            self.main_font.render("MARCE: 1589   DATA: 04/03", True, WHITE), (80, 330)
        )
        self.win.blit(
            self.main_font.render("FERNA:  986   DATA: 04/03", True, WHITE), (80, 370)
        )
        self.win.blit(
            self.main_font.render("TUCA:   265   DATA: 04/03", True, WHITE), (80, 410)
        )
        self.win.blit(
            self.press_font.render("Press space to menu... ", True, WHITE), (150, 470)
        )

        pygame.display.update()
