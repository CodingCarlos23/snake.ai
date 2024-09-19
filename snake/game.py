import pygame
from snake.config import GRID_SIZE, SNAKE_SPEED

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)
        self.food = (300, 200)
        self.score = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, 10):
                    self.direction = (0, -10)
                elif event.key == pygame.K_DOWN and self.direction != (0, -10):
                    self.direction = (0, 10)
                elif event.key == pygame.K_LEFT and self.direction != (10, 0):
                    self.direction = (-10, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-10, 0):
                    self.direction = (10, 0)

    def update(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.running = False

        if new_head in self.snake:
            self.running = False

        self.snake = [new_head] + self.snake[:-1]

        if new_head == self.food:
            self.snake.append(self.snake[-1])  
            self.score += 1
            self.spawn_food()

    def spawn_food(self):
        import random
        self.food = (random.randint(0, (self.width // GRID_SIZE) - 1) * GRID_SIZE,
                     random.randint(0, (self.height // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self):
        self.screen.fill((0, 0, 0))  
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, GRID_SIZE, GRID_SIZE))
        pygame.display.flip()  
