
import random

# TKinter for GUI

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.highScore = 0
        self.gameOver = False
        self.matrix = []
        self.grid()
        self.makeGUI()
        self.startGame()

    def startGame(self):
        self.score = 0
        # Create a matrix of zeros
        # [0] [0] [0] [0]
        # [0] [0] [0] [0]
        # [0] [0] [0] [0]
        # [0] [0] [0] [0]
        self.matrix = [[] * 4 for _ in range(4)]
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrix[row][col] = 2
        while self.matrix[row][col] != 0:
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = 2



    # Matrix Manipulation Functions

    def stack(self): # eliminates empty space for non zeros and move them to one side of the box
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix


    def combine(self):  # join two tiles of same value together and update score
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]


    def reverse(self):  # reverse tiles board
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix


    def transpose(self): # Rows turn to cols and cols turn to rows
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix


    def add_new_tile(self):  # add new 2 0r 4 tile randomly to matrix after every move
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    def makeGUI():
        print("GUI")


    def updateGUI():
        print("GUI")

    # Check if any moves are possible

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False


    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False



    def game_over(self):
        if any(2048 in row for row in self.matrix):
            print("YOu Win!")
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            print("Sorry You did not Win")
        self.highScore = max(self.highScore, self.score)
        self.gameOver = True



    # Arrow-Press Functions

    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

