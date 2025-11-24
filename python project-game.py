
game = input("ENTER 1 FOR NUMBER GUESSING, 2 FOR TIC-TAC-TOE, 3 FOR ROCK-PAPER-SCISSORS,4 hangaman : ")

while game != "1" and game != "2" and game != "3" and game!="4":
    game = input("Invalid input. \nENTER 1 FOR NUMBER GUESSING, 2 FOR TIC-TAC-TOE, 3 FOR ROCK-PAPER-SCISSORS: ")

if game == "1":
    print("so you are playing number guessing game")
    print("-----------------------------------------")
    import random

    low = 1
    high = 100
    answer = random.randint(low, high)
    guess = 0 
    is_running = True
    guesses = 0

    while is_running:
        print("----------------------------------------")
        print(f"number guess game entre your number between {low},{high}")
        guess = input("entre your guess number : ")
        print("-----------------------------------------")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if low > guess or high < guess:
                print("entre your number again ")
                print("your number is of range ")
                print(f"plz select the number between {low} to {high}")
            elif answer > guess:
                print("your number is lower")
            elif answer < guess:
                print("number is higher")
            else:
                print(f"correct number is {answer} total guess are {guesses}")
                print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
                is_running = False
        else:
            print("entre a valid satement ")

elif game == "2":
    print("so you are playing Tic-Tac-Toe")
    print("--------------------------------------")
    
    def display(board):
        print("\n")
        print(f" {board[1]} | {board[2]} | {board[3]} ")
        print("---+---+---")
        print(f" {board[4]} | {board[5]} | {board[6]} ")
        print("---+---+---")
        print(f" {board[7]} | {board[8]} | {board[9]} ")
        print()
    
    def win(board, mark):
        wins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        return any(board[a]==board[b]==board[c]==mark for a,b,c in wins)

    def full(board):
        return all(space != " " for space in board[1:])

    def player_move(board, mark):
        while True:
            try:
                pos = int(input(f"Player {mark}, choose position (1-9): "))
                if pos in range(1,10) and board[pos] == " ":
                    board[pos] = mark
                    return
                print("Invalid position or already taken. Try again.")
            except ValueError:
                print("Please enter a number 1-9.")

    def main():
        print("Tic Tac Toe - Two Players")
        while True:
            board = [" "] * 10
            current = "X"
            display(board)
            while True:
                player_move(board, current)
                display(board)
                if win(board, current):
                    print(f"Player {current} wins!\n")
                    break
                if full(board):
                    print("It's a tie!\n")
                    break
                current = "O" if current == "X" else "X"
            again = input("Play again? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye!")
                break
    
    main()
elif game=="3":
    import random


    words = ["python", "computer", "hangman", "programming", "keyboard", "developer", "software", "internet"]

    print("words that you can guess are  ")
    print("python ","computer","hangman", "programming","keyboard", "developer","software","internet")


    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        print("\n" + display)
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
    
        if "_" not in display:
            print("\nYou won! The word was:", word)
            break
        
    
        guess = input("\nGuess a letter: ").lower()
        
    
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1


    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")


else:
    print("so you are playing rock,paper,scissors")
    print("--------------------------------------")

    import random    
    question = ("rock", "paper", "scissors")  

    running = True
    score = 0 

    while running:
        computer = random.choice(question)
        player = None
        
        while player not in question:
            player = input("Enter a choice (rock, paper, scissors): ").lower()
        
        print("-----------------------------")
        print(f'Player: {player}')
        print(f"Computer: {computer}")
        print("-----------------------------")
        
        if computer == player:
            print("Tie! 🪨📃✂️")
            print("-----------------------------")
        elif player == "rock" and computer == "scissors":
            print("You won! 🪨🪨🪨")
            print("-----------------------------")
            score += 1
        elif player == "paper" and computer == "rock":  
            print("You won! 📃📃")
            print("-----------------------------")
            score += 1
        elif player == "scissors" and computer == "paper":
            print("You won! ✂️✂️✂️")
            print("-----------------------------")
            score += 1
        else:
            print("You lose!")  
            print("-----------------------------")
            score -= 1
        
        if input("Play again? (y/n): ").lower() != "y":
            running = False

    print(f"Your final score: {score}")
