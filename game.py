import os
import pygame

from screens.leaderboard import Leaderboard
from screens.menu import Menu
from screens.play import Play
from screens.profile import Profile
from screens.login import Login

DISPLAY_CAPTION: str = "ABC | 42 Asteroids"

DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 640
FRAMERATE: int = 60

LOGIN: int = 0
MAIN_MENU: int = 1
PLAY: int = 2
LEADERBOARD: int = 3
PROFILE: int = 4
LOGOUT: int = 5
QUIT: int = 6
GAME_OVER: int = 7


class Game:
    def __init__(self: object) -> None:
        pygame.init()

        self.display_caption: str = DISPLAY_CAPTION

        project_dir: str = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir: str = f"{project_dir}/assets"

        self.menu_background_offset: int = 0

        self.screen_width: int = DISPLAY_WIDTH
        self.screen_height: int = DISPLAY_HEIGHT
        self.framerate: int = FRAMERATE

        self.keep_running: bool = True
        self.game_over: bool = False
        self.state: int = MAIN_MENU
        self.menu_state: int = PLAY

        pygame.display.set_caption(self.display_caption)

        self.win = pygame.display.set_mode((self.screen_width, self.screen_height))

    def run(self: object) -> None:
        print("🚀 Running Asteroids' game!")
        login: Login = Login(self.win, self.screen_width, self.screen_height)
        menu: Menu = Menu(self.win, self.assets_dir, self.framerate)
        play: Play = Play(self.win, self.assets_dir, self.framerate)
        leaderboard: Leaderboard = Leaderboard(
            self.win, self.screen_width, self.screen_height
        )
        profile: Profile = Profile(self.win, self.screen_width, self.screen_height)

        clock: pygame.time.Clock = pygame.time.Clock()
        while self.keep_running:
            clock.tick(self.framerate)

            keys: pygame.key = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.keep_running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_running = False

            if self.state == LOGIN:
                self.state = login.run()
            if self.state == MAIN_MENU:
                self.state = menu.run()
            if self.state == PLAY:
                self.state = play.run()
            if self.state == LEADERBOARD:
                self.state = leaderboard.run()
            if self.state == PROFILE:
                self.state = profile.run()
            if self.state == QUIT:
                self.keep_running = False

        if self.game_over:
            print("💥 Game Over!")
        elif not self.keep_running:
            print("🏁 Game Closed.")
        else:
            print("❔ Game Ended with unknown reason!")
