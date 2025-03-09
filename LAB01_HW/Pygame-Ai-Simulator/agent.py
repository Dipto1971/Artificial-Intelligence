import pygame

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
AGENT_SIZE = (30, 30)
AGENT1_COLOR = (0, 128, 255)  # Blue
AGENT2_COLOR = (255, 0, 0)  # Red

class Agent(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, controls):
        super().__init__()
        self.image = pygame.Surface(AGENT_SIZE)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_x, start_y
        self.speed = 5
        self.controls = controls

    def update(self, keys, other_agents):
        """Update the agent's position while avoiding collisions."""
        new_x, new_y = self.rect.x, self.rect.y

        # Simulate movement
        if keys[self.controls["left"]] and self.rect.left > 0:
            new_x -= self.speed
        if keys[self.controls["right"]] and self.rect.right < WINDOW_WIDTH:
            new_x += self.speed
        if keys[self.controls["up"]] and self.rect.top > 0:
            new_y -= self.speed
        if keys[self.controls["down"]] and self.rect.bottom < WINDOW_HEIGHT:
            new_y += self.speed

        # Create a temporary rect to check collisions
        new_rect = self.rect.move(new_x - self.rect.x, new_y - self.rect.y)

        # Check if moving would cause a collision
        if not any(new_rect.colliderect(agent.rect) for agent in other_agents):
            self.rect.x, self.rect.y = new_x, new_y