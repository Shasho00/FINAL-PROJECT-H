import pygame

WINDOW_NAME = "Hit The Target"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True

# גדלים
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
TARGET_SIZES = (50, 38)
TARGET_SIZE_RANDOMIZE = (1,2) # יכפיל את גודל המטרה בX Y


# להראות את הHITBOX
DRAW_HITBOX = False

# אנימציה 
ANIMATION_SPEED = 0.08 # מהירות של התזוזה של המטרה

# רמת קושי
GAME_DURATION = 60 # זמן שירוץ המשחק
TARGET_SPAWN_TIME = 2.5
TARGET_MOVE_SPEED = {"min": 1, "max": 5}

# צבע
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}}

# סאוונדים 
MUSIC_VOLUME = 0.16 
SOUNDS_VOLUME = 1

# טקסט
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
