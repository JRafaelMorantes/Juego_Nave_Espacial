import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/ship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Bullet/ice_bullet.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
CALATRAMIX = pygame.image.load(os.path.join(IMG_DIR, "Enemy/calatramix.png"))
COVENANT = pygame.image.load(os.path.join(IMG_DIR, "Enemy/covenant.png"))
ICON_OF_SIN = pygame.image.load(os.path.join(IMG_DIR, "Enemy/icon_of_sin.png"))
DIABOLIC_SPACE_PRIEST = pygame.image.load(os.path.join(IMG_DIR, "Enemy/diabolic_space_priest.png"))
SLAYER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/slayer_space.png"))
HELLHAMMER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/hellhammer.png"))
RECRUITER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/recruiter.png"))
ULDAMAR = pygame.image.load(os.path.join(IMG_DIR, "Enemy/uldamar.png"))
ELITE_HELL = pygame.image.load(os.path.join(IMG_DIR, "Enemy/elite_hell.png"))

FONT_STYLE = 'freesansbold.ttf'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'