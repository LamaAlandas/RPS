#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
# imports
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    # keep track of score and initialize attributes
    def __init__(self):
        self.score = 0
        self.mylastmove = random.choice(moves)
        self.opponentlastmove = random.choice(moves)

    def move(self):
        return "rock"

    # learn function implementation
    def learn(self, my_move, their_move):
        self.mylastmove = my_move
        self.opponentlastmove = their_move

# RandomPlayer class


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))

# ReflectPlayer class


class ReflectPlayer(Player):
    def move(self):
        return (self.opponentlastmove)

# CyclePlayer class


class CyclePlayer(Player):

    def move(self):
        if self.mylastmove == 'rock':
            return 'paper'

        elif self.mylastmove == 'paper':
            return 'scissors'

        else:
            'rock'

# HumanPlayer class


class HumanPlayer(Player):

    def move(self):
        while True:
            humaninput = input(
                "Enter the move you want to make"
                "(rock, paper, scissors): ").lower()
            if humaninput == 'rock':
                return 'rock'
            elif humaninput == 'paper':
                return 'paper'
            elif humaninput == 'scissors':
                return 'scissors'
            else:
                print(f"Incorrect input. Please, try again\n")


# no need to change this function
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # to find out who is the winner of the current round
        if beats(move1, move2):
            self.p1.score += 1
            print(f"Player 1 won this round!")
        elif beats(move2, move1):
            self.p2.score += 1
            print(f"Player 2 won this round!")
        else:
            print(f"It is a tie this time!")

        print(
            f"Player 1 score is: {self.p1.score}"
            "Player 2 score is: {self.p2.score}")

    def play_game(self):
        print(f"\nGame start!\n")

        for round in range(3):
            print(f"Round {round}:")
            self.play_round()

        print(f"\nGame over!\n")

        # show who won the game
        if self.p1.score > self.p2.score:
            print(f"Player 1 is the winner!")
        elif self.p2.score > self.p1.score:
            print(f"Player 2 is the winner!")
        else:
            print("It is a tie!")

        print(
            f"Player 1 score is: {self.p1.score}"
            "  Player 2 score is: {self.p2.score}")


# interface (edited)
if __name__ == '__main__':

    while True:
        userinput = input(
                f"\nSelect your desired option from the"
                "below by entering the option number:"
                f"\n1. You vs a rocker player.\n2. you"
                f"vs random player.\n"
                f"3. you vs a reflect player.\n4. you vs"
                f"cycle player.\nIf you want to quit the game,"
                f"type q\nYour choice is: ").lower()

        if userinput == "1":
            game = Game(HumanPlayer(), Player())
        elif userinput == "2":
            game = Game(HumanPlayer(), RandomPlayer())
        elif userinput == "3":
            game = Game(HumanPlayer(), ReflectPlayer())
        elif userinput == "4":
            game = Game(HumanPlayer(), CyclePlayer())
        elif userinput == "q":
            exit()
        else:
            print(f"Invalid entery. Please, try again.\n")

        game.play_game()
