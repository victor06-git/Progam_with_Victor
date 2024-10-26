import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pac-Man Game")

# Map layout
MAP = [
    "####################",
    "#                  #",
    "#  #######  ###### #",
    "#      #        # #",
    "###### # ####### # #",
    "#      #        # #",
    "#  #######  ###### #",
    "#                  #",
    "####################"
]

TILE_SIZE = 20

# Pac-Man class
class PacMan:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 15
        self.speed = 5

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        # Check bounds with the map
        if self.can_move(new_x, self.y):
            self.x = new_x
        if self.can_move(self.x, new_y):
            self.y = new_y

    def can_move(self, x, y):
        # Check if the position is within the bounds of the map
        map_x = x // TILE_SIZE
        map_y = y // TILE_SIZE
        
        # Ensure map_x and map_y are within the valid range
        if map_x < 0 or map_x >= len(MAP[0]) or map_y < 0 or map_y >= len(MAP):
            return False
        
        if MAP[map_y][map_x] == '#':
            return False
        return True

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.radius = 5

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# Ghost class
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.speed = 3

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def move(self):
        # Simple AI to move the ghost towards Pac-Man
        if pacman.x > self.x:
            self.x += self.speed
        elif pacman.x < self.x:
            self.x -= self.speed
        if pacman.y > self.y:
            self.y += self.speed
        elif pacman.y < self.y:
            self.y -= self.speed

        # Keep ghost within bounds
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

# Main game loop
def main():
    clock = pygame.time.Clock()
    global pacman  # Make pacman global to access in Ghost class
    pacman = PacMan()
    food = Food()
    ghost = Ghost(100, 100)  # Start ghost at a fixed position
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -pacman.speed
        if keys[pygame.K_RIGHT]:
            dx = pacman.speed
        if keys[pygame.K_UP]:
            dy = -pacman.speed
        if keys[pygame.K_DOWN]:
            dy = pacman.speed

        pacman.move(dx, dy)

        # Check for collision with food
        if (pacman.x - food.x) ** 2 + (pacman.y - food.y) ** 2 < (pacman.radius + food.radius) ** 2:
            score += 1
            food = Food()  # Respawn food

        # Move the ghost
        ghost.move()

        # Drawing
        screen.fill(BLACK)
        
        # Draw the map
        for y, row in enumerate(MAP):
            for x, tile in enumerate(row):
                if tile == '#':
                    pygame.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE , TILE_SIZE, TILE_SIZE))

        pacman.draw()
        food.draw()
        ghost.draw ()
        pygame.display.flip()

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()