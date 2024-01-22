'''

@Author: Joshikaran

@Date: 2024-01-22 16:30:00

@Last Modified by:Joshikaran

@Last Modified time: 2024-01-20 16:30:00

@Title : solving Snake and ladder Program

'''



import random

class snake_andladder():


    def __init__(self):
        self.player_position =0
        self.roll = 0
        self.board = ["Snake","No_Play","Ladder"]

    def roll_dice(self) -> int:
        self.roll=random.randint(0,6)
        if self.roll > 0 and self.player_position<=100:
            self.player_position += self.roll
        return self.player_position
    
    def board_place(self):
        bord = random.choice(self.board)
        if bord == self.board[0]:
            self.player_position -= self.roll
        elif bord == self.board[1]:
            self.player_position += 0
        if bord == self.board[2]:
            self.player_position += self.roll
        return (f"position: {self.player_position}")


if __name__ == "__main__":
    obj1=snake_andladder()
    print(obj1.roll_dice())
    print(obj1.board_place())