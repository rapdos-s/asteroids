import os
import pygame

from game import Game

MAIN_FONT_SIZE: int = 25


def setup():
    print("\n🎮 Setting up Asteroids' game... ")

    pygame.init()

    display_caption: str = "ABC | 42 Asteroids"

    project_dir: str = os.path.dirname(os.path.abspath(__file__))
    assets_dir: str = f"{project_dir}/assets"
    background_image: pygame.Surface = pygame.image.load(f"{assets_dir}/background.png")
    player_rocket: pygame.Surface = pygame.image.load(f"{assets_dir}/player_rocket.png")
    game_over: pygame.Surface = pygame.image.load(f"{assets_dir}/game_over.png")

    menu_background: pygame.Surface = pygame.image.load(
        f"{assets_dir}/full_background.png"
    )
    main_menu_border: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_border.png"
    )
    main_menu_none_selected: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_none_selected.png"
    )
    main_menu_play_selected: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_play_selected.png"
    )
    main_menu_highscore_selected: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_highscore_selected.png"
    )
    main_menu_profile_selected: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_profile_selected.png"
    )
    main_menu_quit_selected: pygame.Surface = pygame.image.load(
        f"{assets_dir}/main_menu_quit_selected.png"
    )

    main_font: pygame.font.Font = pygame.font.Font(
        f"{assets_dir}/Adventure_ReQuest.ttf", MAIN_FONT_SIZE
    )

    game: Game = Game(
        display_caption=display_caption,
        background_image=background_image,
        player_rocket=player_rocket,
        game_over=game_over,
        menu_background=menu_background,
        main_menu_border=main_menu_border,
        main_menu_none_selected=main_menu_none_selected,
        main_menu_play_selected=main_menu_play_selected,
        main_menu_highscore_selected=main_menu_highscore_selected,
        main_menu_profile_selected=main_menu_profile_selected,
        main_menu_quit_selected=main_menu_quit_selected,
        main_font=main_font,
    )

    print("🎮 Asteroids' game is ready!")
    return game


if __name__ == "__main__":
    game: Game = setup()

    game.run()

    print("🌌 Everything is done, Bye!")
