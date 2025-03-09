import pygame

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation Framework")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)