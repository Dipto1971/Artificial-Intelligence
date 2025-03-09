import pygame
import sys
from agent import Agent, AGENT1_COLOR, AGENT2_COLOR
from environment import screen, clock, font, BACKGROUND_COLOR, TEXT_COLOR

# Create two agents with different controls
agent1 = Agent(AGENT1_COLOR, 100, 100, {
    "left": pygame.K_LEFT, "right": pygame.K_RIGHT,
    "up": pygame.K_UP, "down": pygame.K_DOWN
})

agent2 = Agent(AGENT2_COLOR, 200, 200, {
    "left": pygame.K_a, "right": pygame.K_d,
    "up": pygame.K_w, "down": pygame.K_s
})

# Group all sprites
all_sprites = pygame.sprite.Group(agent1, agent2)
agents = [agent1, agent2]  # List for collision detection

# Main loop
running = True
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update both agents while checking for collisions
    for agent in agents:
        other_agents = [a for a in agents if a != agent]  # Exclude itself
        agent.update(keys, other_agents)

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw agents
    all_sprites.draw(screen)

    # Display the frame count as debug info
    frame_text = font.render(f"Frame: {pygame.time.get_ticks() // 1000}", True, TEXT_COLOR)
    screen.blit(frame_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()