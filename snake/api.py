from snake.game import SnakeGame

class SnakeAPI:
    def __init__(self):
        self.game = SnakeGame()

    def reset(self):
        self.game.__init__() 

    def step(self, action):
        if action == 0:
            self.game.direction = (0, -10)
        elif action == 1:
            self.game.direction = (0, 10)
        elif action == 2:
            self.game.direction = (-10, 0)
        elif action == 3:
            self.game.direction = (10, 0)

        self.game.update()
        return self.game.snake, self.game.food, self.game.score, not self.game.running  

    def get_state(self):
        return self.game.snake, self.game.food, self.game.score
