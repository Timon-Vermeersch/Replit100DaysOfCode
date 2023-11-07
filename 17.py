print("LOCAL VERSUS ROCK PAPER SCISSOR")
print("")

victoryusername1 = 0
victoryusername2 = 0

templatechoice = str("""
1. Rock
2. Paper
3. Scissor
""")

scoreusername1 = 0
scoreusername2 = 0

username1 = input("What's your name player 1?: ")
print("")
username2 = input("And player 2's name?: ")
print("")

print(username1, "you are player 1,", username2, "you are player 2")
print("")

while True:
    print(username1, '?')
    answer1 = input(templatechoice)

    # Check if the input is valid (1, 2, 3, Rock, Paper, or Scissor)
    valid_inputs = ['1', '2', '3', 'Rock', 'Paper', 'Scissor']
    if answer1 not in valid_inputs:
        print("Invalid input. Please choose 1, 2, or 3 for Rock, Paper, or Scissor.")
        continue  # Restart the loop

    print(username2, '?')
    answer2 = input(templatechoice)
    print("")

    # Convert user-friendly inputs to numerical values (1, 2, 3)
    if answer1 in ['Rock', 'rock']:
        answer1 = '1'
    elif answer1 in ['Paper', 'paper']:
        answer1 = '2'
    elif answer1 in ['Scissor', 'scissor']:
        answer1 = '3'

    if answer2 in ['Rock', 'rock']:
        answer2 = '1'
    elif answer2 in ['Paper', 'paper']:
        answer2 = '2'
    elif answer2 in ['Scissor', 'scissor']:
        answer2 = '3'

    # Determine the winner
    if answer1 == answer2:
        print("It's a tie!")
    elif (answer1 == '1' and answer2 == '3') or (answer1 == '2' and answer2 == '1') or (answer1 == '3' and answer2 == '2'):
        print(username1, "won this round.")
        scoreusername1 += 1
    else:
        print(username2, "won this round.")
        scoreusername2 += 1

    print("")
    print("Current scores:")
    print(username1, scoreusername1)
    print(username2, scoreusername2)

    doorgaan = input("Continue? (yes/no): ")
    if doorgaan.lower() == 'no':
        break
