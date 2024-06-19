from typing import Tuple

# Display
DISPLAY_CAPTION: str = "ABC | 42 Asteroids"
DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 640
DISPLAY_FRAMERATE: int = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (11, 17, 29)
YELLOW = (236, 255, 21)

# Fonts
ANTIALIAS: bool = True

# Menu States
LOGIN: int = 0
MAIN_MENU: int = 1
PLAY: int = 2
LEADERBOARD: int = 3
PROFILE: int = 4
LOGOUT: int = 5
QUIT: int = 6
GAME_OVER: int = 7

# Score
SCORE_TEXT: str = "Score: "
SCORE_FONT_SIZE: int = 25
SCORE_X: int = 42
SCORE_Y: int = 24
SCORE_COLOR: tuple = (242, 242, 142)

# Game Over
GAME_OVER_MESSAGE_TEXT: str = "Press space to continue..."
GAME_OVER_MESSAGE_FONT_SIZE: int = 25
GAME_OVER_MESSAGE_COLOR: tuple = (242, 242, 142)

# Asteroids
ASTEROID_COLLISION_REDUCER: float = 0.7
ASTEROID_TIME_SPAWN: int = 1000
ASTEROID_LIMIT: int = 10
ASTEROID_SMALL_SIZE: int = 1
ASTEROID_MEDIUM_SIZE: int = 2
ASTEROID_BIG_SIZE: int = 4
ASTEROID_SMALL_POINTS: int = 1000
ASTEROID_MEDIUM_POINTS: int = 500
ASTEROID_BIG_POINTS: int = 200

# Player
PLAYER_COLLISION_REDUCER: float = 0.2
PLAYER_TURN_SPEED: int = 2
PLAYER_START_ANGLE: int = 0
PLAYER_MOVE_SPEED: int = 4

# Bullet
BULLET_SIZE: int = 5
BULLET_SPEED: int = 15
BULLET_COLOR: Tuple[int, int, int] = (242, 242, 142)
