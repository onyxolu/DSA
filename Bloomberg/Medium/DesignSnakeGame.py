

from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food):
        
        # initiailize your data structure here
        # width = screen width
        # height = screen height
        # food = a list of food positions
        # E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1] and second at [1,0]
        self.width = width
        self.height = height
        self.food = food
        self.queue = deque([(0,0)])
        self.score = 0
        
        

    def move(self, direction: str) -> int:
        # moves the snake
        # Direction - U=Up, L=Left, R-Right , D=Down
        # Return the game score after the move, return -1 if game over
        # game over when snake crosses the screen boundary or bites its body
        
        head_r, head_c = self.queue[-1]
        
        if direction == 'U':
            head_r -= 1
        elif direction == 'L':
            head_c -= 1
        elif direction == 'R':
            head_c += 1
        elif direction == 'D':
            head_r += 1
            
        if head_r < 0 or head_r > self.height - 1 or head_c < 0 or head_c > self.width - 1:
            return -1
        
        if self.food and [head_r, head_c] == self.food[0]:
            self.queue.append([head_r, head_c])
            self.food.pop(0)
            self.score += 1
        else:
            self.queue.popleft()
            
            if [head_r, head_c] in self.queue:
                return -1
            else:
                self.queue.append([head_r, head_c])
                
        return self.score
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)