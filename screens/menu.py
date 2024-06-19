import pygame

from constants import *

from screens.screen import Screen


class Menu(Screen):
    def __init__(
        self: object,
        win: pygame.Surface,
        assets_dir: str,
        framerate: int,
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate = framerate

        self.border: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_border.png"
        )
        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/full_background.png"
        )
        self.main_menu_play_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_play_selected.png"
        )
        self.main_menu_leaderboard_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_leaderboard_selected.png"
        )
        self.main_menu_profile_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_profile_selected.png"
        )
        self.main_menu_logout_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_logout_selected.png"
        )
        self.main_menu_quit_selected: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/main_menu_quit_selected.png"
        )

        self.background_image_width: int = self.background.get_width()

        self.menu_background_offset: int = 0

        self.menu_state: int = PLAY

    def run(self: object) -> int:
        clock: pygame.time.Clock = pygame.time.Clock()
        selected: bool = False
        self.menu_state = PLAY

        while not selected:
            clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selected = True
                    self.menu_state = QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.menu_state -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.menu_state += 1
                    elif event.key == pygame.K_RETURN:
                        selected = True
                    elif event.key == pygame.K_ESCAPE:
                        selected = True
                        self.menu_state = LOGOUT

            if self.menu_state < PLAY:
                self.menu_state = QUIT
            elif self.menu_state > QUIT:
                self.menu_state = PLAY

            if selected is False:
                self.draw()

        return self.menu_state

    def draw(self: object) -> None:
        self.win.blit(self.background, (self.menu_background_offset, 0))
        self.win.blit(
            self.background,
            (self.menu_background_offset + self.background_image_width, 0),
        )

        rect_width: int = 300
        rect_height: int = 255
        rect_radius: int = 20
        rect_x: int = self.win.get_width() // 2 - rect_width // 2
        rect_y: int = 340
        rect_color: tuple = (0, 0, 0)
        rect_alpha: int = 128

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

        if self.menu_state == PLAY:
            self.win.blit(self.main_menu_play_selected, (0, 0))
        elif self.menu_state == LEADERBOARD:
            self.win.blit(self.main_menu_leaderboard_selected, (0, 0))
        elif self.menu_state == PROFILE:
            self.win.blit(self.main_menu_profile_selected, (0, 0))
        elif self.menu_state == LOGOUT:
            self.win.blit(self.main_menu_logout_selected, (0, 0))
        elif self.menu_state == QUIT:
            self.win.blit(self.main_menu_quit_selected, (0, 0))

        self.win.blit(self.border, (0, 0))

        pygame.display.update()

        self.menu_background_offset -= 1
        if self.menu_background_offset < 0 - self.background_image_width:
            self.menu_background_offset = 0
