import pygame
import random

from constants import *

from screens.resources.player import Player
from screens.screen import Screen
from screens.resources.asteroid import Asteroid


class Play(Screen):
    def __init__(
        self: object, win: pygame.Surface, assets_dir: str, framerate: int
    ) -> None:
        self.win: pygame.Surface = win
        self.assets_dir: str = assets_dir
        self.framerate = framerate

        self.background: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/background.png"
        )
        self.game_over_image: pygame.Surface = pygame.image.load(
            f"{self.assets_dir}/game_over.png"
        )

        self.score_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )
        self.game_over_title_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )
        self.game_over_message_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/Adventure_ReQuest.ttf", SCORE_FONT_SIZE
        )
        self.game_over_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 65
        )
        self.press_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 25
        )
        self.debug_font: pygame.font.Font = pygame.font.Font(
            f"{self.assets_dir}/04B_03__.ttf", 20
        )

        self.player: Player = Player(
            x=self.win.get_width() // 2,
            y=self.win.get_height() // 2,
            display_width=self.win.get_width(),
            display_height=self.win.get_height(),
            assets_dir=self.assets_dir,
        )

        self.asteroids: list[Asteroid] = []

        self.score: int = 0
        self.limit_score: int = 0
        self.game_over: bool = False
        self.asteroid_timer: int = 0
        self.debug: bool = False
        self.asteroids_destroyed: int = 0

        self.achievement_debug: bool = False

    def __del__(self: object):
        pass

    def run(self: object) -> int:
        self.score = 0
        self.game_over = False
        self.asteroids_destroyed = 0

        # Verifica se já jogou antes

        keep_running: bool = True
        return_state: int = MAIN_MENU
        clock: pygame.time.Clock = pygame.time.Clock()

        while keep_running:
            delta_time: float = clock.tick(self.framerate)

            if self.game_over == False:
                self.player.check_movement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_running = False
                    return_state = QUIT
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keep_running = False
                        return_state = MAIN_MENU
                    if event.key == pygame.K_k:
                        self.game_over = True
                    if event.key == pygame.K_SPACE:
                        if self.game_over == False:
                            self.player.shoot()
                        if self.game_over == True:
                            keep_running = False
                            return_state = MAIN_MENU
                    if event.key == pygame.K_1:
                        self.debug = not self.debug

            for bullet in self.player.bullets:
                if bullet.off_screen(self.win):
                    self.player.bullets.pop(self.player.bullets.index(bullet))
                elif self.game_over == False:
                    bullet.move()

                for asteroid in self.asteroids:
                    if bullet.get_collision().colliderect(asteroid.get_collision()):
                        try:
                            self.player.bullets.pop(self.player.bullets.index(bullet))
                            self.score += asteroid.get_points()
                            if asteroid.get_size() != ASTEROID_SMALL_SIZE:
                                self.asteroids.append(
                                    Asteroid(
                                        self.win,
                                        self.assets_dir,
                                        size=asteroid.get_size() // 2,
                                        x=asteroid.get_x(),
                                        y=asteroid.get_y(),
                                    )
                                )
                                self.asteroids.append(
                                    Asteroid(
                                        self.win,
                                        self.assets_dir,
                                        size=asteroid.get_size() // 2,
                                        x=asteroid.get_x(),
                                        y=asteroid.get_y(),
                                    )
                                )
                            self.asteroids.pop(self.asteroids.index(asteroid))
                            self.asteroids_destroyed += 1
                        except:
                            pass

            for asteroid in self.asteroids:
                if asteroid.off_screen(self.win) or asteroid.is_destroyed():
                    self.asteroids.pop(self.asteroids.index(asteroid))
                elif self.game_over == False:
                    asteroid.move()

                if asteroid.get_collision().colliderect(self.player.get_collision()):
                    self.game_over = True

            self.asteroid_timer += delta_time
            if (
                self.asteroid_timer > ASTEROID_TIME_SPAWN
                and len(self.asteroids) < ASTEROID_LIMIT
            ):
                self.asteroids.append(
                    Asteroid(
                        self.win,
                        self.assets_dir,
                        size=random.choice(
                            [
                                ASTEROID_SMALL_SIZE,
                                ASTEROID_MEDIUM_SIZE,
                                ASTEROID_BIG_SIZE,
                            ]
                        ),
                    )
                )
                self.asteroid_timer = 0

            if keep_running == True:
                self.draw()

        for asteroid in self.asteroids:
            self.asteroids.pop(self.asteroids.index(asteroid))

        return return_state

    def draw(self: object) -> None:
        self.draw_background()
        self.draw_bullets()
        self.draw_player()
        self.draw_asteroid()
        self.draw_score()
        self.draw_game_over()

        if self.debug == True:
            self.draw_debug()

        pygame.display.update()

    def draw_background(self: object) -> None:
        self.win.blit(self.background, (0, 0))

    def draw_player(self: object) -> None:
        self.player.draw(self.win)

    def draw_asteroid(self: object) -> None:
        for asteroid in self.asteroids:
            asteroid.draw(self.win)

    def draw_bullets(self: object) -> None:
        for bullet in self.player.bullets:
            bullet.draw(self.win)

    def draw_score(self: object) -> None:
        score_text: str = f"{SCORE_TEXT}{self.score}"

        text: pygame.Surface = self.score_font.render(score_text, ANTIALIAS, WHITE)

        self.win.blit(text, (SCORE_X, SCORE_Y))
        if self.limit_score % 10 == 0 and self.game_over == False:
            self.score += 1
        self.limit_score += 1

    def draw_game_over(self: object) -> None:
        if self.game_over:
            self.game_over = True
            rect_width: int = 640
            rect_height: int = 640
            rect_radius: int = 0
            rect_x: int = 0
            rect_y: int = 0
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

            self.win.blit(
                self.game_over_font.render("GAME OVER", True, YELLOW), (147, 267)
            )
            self.win.blit(
                self.press_font.render("Press space to menu... ", True, WHITE),
                (170, 350),
            )

    def draw_debug(self: object) -> None:
        if self.achievement_debug == False or True:
            self.draw_achievements(
                icon=f"{self.assets_dir}/icon.png",
                title="What's this?",
                description="Visualize the debug mode.",
            )
            self.achievement_debug = True

        self.player.draw_collision(self.win)

        for asteroid in self.asteroids:
            asteroid.draw_collision(self.win)

        text_y: int = 10
        text_y_line: int = 20
        text_x: int = 10

        texts: list[str] = [
            f"DEBUG MODE: Activated",
            f"",
            f"Asteroids: {len(self.asteroids)}",
            f"Bullets: {len(self.player.bullets)}",
            f"",
            f"Player position: {self.player.get_x():.2f}, {self.player.get_y():.2f}",
            f"Player angle: {self.player.get_angle()}",
            f"",
            f"Asteroids destroyed: {self.asteroids_destroyed}",
        ]

        for text in texts:
            text_surface: pygame.Surface = self.debug_font.render(
                text, ANTIALIAS, YELLOW
            )
            text_width: int = text_surface.get_width()
            right_align_x: int = DISPLAY_WIDTH - text_width - text_x
            self.win.blit(text_surface, (right_align_x, text_y))
            text_y += text_y_line
