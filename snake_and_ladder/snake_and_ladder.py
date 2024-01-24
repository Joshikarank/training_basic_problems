'''

@Author: Joshikaran.k

@Date: 2024-01-23 10:30:00

@Last Modified by: Joshikaran.k

@Last Modified time: 2024-01-23 10:30:00

@Title : Creating Snake Ladder Program

'''


import random
class Player:
    def _init_(self):
        self.position=0

    def move_position(self):
        dice=random.randint(1,6)
        options=["snake","ladder","no play"]
        extra_chance=True
        while extra_chance and self.position!=100:
            option=random.choice(options)
            if option=="snake":
                self.position-=dice
                if self.position<0:
                    self.position=0
                extra_chance=False 
            elif option=="ladder":
                if self.position+dice<=100:
                    self.position+=dice
            else:
                extra_chance=False


class Game:
    def _init_(self,player1,player2):
        self.player1=player1
        self.player2=player2
    def start_game(self):
        print("*")
        print("Welcome to the Snake and Ladder Program")
        player=random.randint(0,1)
        dice_count=0
        while self.player1.position!=100 and self.player2.position!=100:
            if player==0:
                self.player1.move_position()
            if player==1:
                self.player2.move_position()
            dice_count+=1
            player=(player+1)%2
        if self.player1.position==100:
                print("Player 1 won the game")
        if self.player2.position==100:
            print("Player 2 won the game")
        print(f"Player 1 is at position {self.player1.position}")
        print(f"Player 2 is at position {self.player2.position}")
        print(f"The dice rolled for {dice_count} times")
        print("*")



if __name__=="__main__":
    p1=Player()
    p2=Player()
    snake_and_Ladder=Game(p1,p2)
    snake_and_Ladder.start_game()