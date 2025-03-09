import pygame
# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
AGENT_SIZE = (30, 30)

class Agent(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, controls):
        super().__init__()
        self.image = pygame.Surface(AGENT_SIZE)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_x, start_y
        self.speed = 5
        self.controls = controls

    def update(self, keys):
        """Update the agent's position based on key input."""
        if keys[self.controls["left"]] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[self.controls["right"]] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
        if keys[self.controls["up"]] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.controls["down"]] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed