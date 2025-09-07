import random

print("ROCK PAPER SCISSORS GAME")
print("=" * 40)

player_score = 0
computer_score = 0
rounds = 0

while True:
    print(f"\nRound {rounds + 1}")
    print("-" * 20)
    print("1. Rock")
    print("2. Paper") 
    print("3. Scissors")
    print("4. Quit Game")
    
    choice = input("Choose your move (1-4): ")
    
    while choice not in ['1', '2', '3', '4']:
        choice = input("Invalid choice! Please enter 1, 2, 3, or 4: ")
    
    if choice == '4':
        print('GAME OVER!')
        print(f"Final Score - You: {player_score}, Computer: {computer_score}")
        if player_score > computer_score:
            print("You won the game!")
        elif computer_score > player_score:
            print("Computer won the game!")
        else:
            print("It's a tie!")
        break
    
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    player_move = choices[int(choice)]
    
    computer_choice = random.randint(1, 3)
    computer_move = choices[computer_choice]
    
    print(f"\nYou chose: {player_move}")
    print(f"Computer chose: {computer_move}")
    
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == "Rock" and computer_move == "Scissors") or \
         (player_move == "Paper" and computer_move == "Rock") or \
         (player_move == "Scissors" and computer_move == "Paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    rounds += 1
    
    print(f"\nCurrent Score - You: {player_score}, Computer: {computer_score}")
    
    play_again = input("\nPlay another round? (y/n): ").lower()
    while play_again not in ['y', 'yes', 'n', 'no']:
        play_again = input("Please enter 'y' for yes or 'n' for no: ").lower()
    
    if play_again in ['n', 'no']:
        print("GAME OVER!")
        print(f"Final Score - You: {player_score}, Computer: {computer_score}")
        if player_score > computer_score:
            print("You won the game!")
        elif computer_score > player_score:
            print("Computer won the game!")
        else:
            print("It's a tie!")
        break

print("\nThanks for playing!")
