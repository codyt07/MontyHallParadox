import random

class MontyHallParadox:

    def __init__(self):
        # For the score board
        self.win_count = 0
        self.loss_count = 0 
        self.switched_count = 0
    
    def welcome(self):
        print(f'''\nWelcome to Cody\'s Monty Hall Paradox Game!
            \rSelect one of three doors labeled 1 - 3.
            \rThe Host will open an empty random door.
            \rYou will be given the chance to select a new door
            \rOr Keep your choice.
            \rOne of the remaining doors is the winner!''')
        
    def play(self):
        while True:
            # Generate the winning door
            self.answer = random.randint(1, 3)
            # Exit the program
            self.guess = self.get_user_guess()
            if self.guess == 'q':
                self.end_game()
                break
            # Check the answer compared to the guess
            self.evaluate_choice()

    def get_user_guess(self):
        while True:
            self.guess = input('''\nPick a door number between 1 - 3, 
or enter 'q' to quit: ''').lower()
            if self.guess == 'q' or self.guess.isdigit() and 1 <= int(self.guess) <= 3:
                return self.guess
            print("Invalid input. Please enter a number between 1 and 3 or 'q' to quit.")

    def evaluate_choice(self):
        self.doors = [1, 2, 3]
        self.doors.remove(self.answer)
        if int(self.answer) == int(self.guess):
            self.opened_door = random.choice(self.doors)
            self.same_guess_same_answer()
        else:
            self.doors.remove(int(self.guess))
            self.opened_door = self.doors[0]
            self.diff_guess_diff_answer()
    
    def same_guess_same_answer(self):
        while True:
            print(f'''We have opened {self.opened_door}! It is empty!
            \rDo you want to change doors? You selected door {self.guess} ''')
            switch_doors = input("Enter Y or N: ")
            if switch_doors.lower() == 'y':
                win = False
                switch = True
                self.end_round(win, switch)
                break
            elif switch_doors.lower() == 'n':
                win = True
                switch = False
                self.end_round(win, switch)
                break
            else:
                print("-- Invalid input! --\r")
        
    def diff_guess_diff_answer(self):
        while True:
            print(f'''We have opened {self.opened_door}! It is empty!
            \rDo you want to change doors? You selected door {self.guess} ''')
            switch_doors = input("Enter Y or N: ")
            if switch_doors.lower() == 'y':
                win = True
                switch = True
                self.end_round(win, switch)
                break
            elif switch_doors.lower() == 'n':
                win = False
                switch = False
                self.end_round(win, switch)
                break
            else:
                print("-- Invalid input! --\r")

    def end_round(self, win, switch):
        if switch == True:
            self.switched_count = self.switched_count + 1
        if win == True:
            print(f''' *''' * 16)  
            print(f'''\rCongratulations! You selected the correct door!''')
            self.win_count = self.win_count + 1
        else:
            print(f'''-''' * 16)
            print(f'''\rSorry! Door: {self.answer} was correct!''')
            self.loss_count = self.loss_count + 1
        print (f"Wins: {self.win_count} / Loss {self.loss_count} : Switched doors: {self.switched_count}\r")
    
    def end_game(self):
        print(f"Thanks for playing! Ending Score Below!")
        print (f"Wins: {self.win_count} / Loss {self.loss_count} : Switched doors: {self.switched_count}\r")

if __name__ == '__main__':
    game = MontyHallParadox()
    game.welcome()
    game.play()
