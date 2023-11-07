#https://www.youtube.com/watch?v=8XHcmA7spX0&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=71
#TopTrumpsBattles
import random
import os,time

cards = [
    {"name": "Cho Chang", "Magic": 45, "Cunning": 8, "Courage": 31, "Wisdom": 35, "Temper": 3},
    {"name": "Harry Potter", "Magic": 70, "Cunning": 9, "Courage": 85, "Wisdom": 60, "Temper": 6},
    {"name": "Hermione Granger", "Magic": 65, "Cunning": 10, "Courage": 75, "Wisdom": 90, "Temper": 4},
    {"name": "Ron Weasley", "Magic": 50, "Cunning": 7, "Courage": 70, "Wisdom": 40, "Temper": 5},
    {"name": "Draco Malfoy", "Magic": 55, "Cunning": 8, "Courage": 25, "Wisdom": 30, "Temper": 2},
    {"name": "Luna Lovegood", "Magic": 60, "Cunning": 6, "Courage": 45, "Wisdom": 75, "Temper": 3},
    {"name": "Neville Longbottom", "Magic": 40, "Cunning": 5, "Courage": 60, "Wisdom": 50, "Temper": 4},
    {"name": "Severus Snape", "Magic": 80, "Cunning": 10, "Courage": 50, "Wisdom": 90, "Temper": 2},
    {"name": "Ginny Weasley", "Magic": 55, "Cunning": 7, "Courage": 75, "Wisdom": 65, "Temper": 6},
    {"name": "Sirius Black", "Magic": 70, "Cunning": 9, "Courage": 80, "Wisdom": 50, "Temper": 7},
    {"name": "Albus Dumbledore", "Magic": 95, "Cunning": 10, "Courage": 95, "Wisdom": 100, "Temper": 5},
    {"name": "Bellatrix Lestrange", "Magic": 90, "Cunning": 9, "Courage": 80, "Wisdom": 60, "Temper": 8}
     

]

def printList():
    print("Choose Your Champion:")
    for i, character in enumerate(cards, start=1):
        print(f"{i}. {character['name']}")

def pickCharacter():
    while True:
        choice = input("> ")
        if choice.isdigit():
            choice = int(choice)
            if -1 <= choice < len(cards)+1:
                break
            else:
                print("Enter a valid number")
        else:
            print("Enter a valid number")
    return choice

def extraSetup(choice):
    print("")
    player_character = cards[choice - 1]
    computer_candidates = [character for character in cards if character != player_character]
    computer_character = random.choice(computer_candidates)
    player_character_name = player_character["name"]
    computer_character_name = computer_character["name"]
    print(f"You picked: {player_character_name}")
    print(f"AI picked: {computer_character_name}")

    return player_character, computer_character

def pickCategory():
    print("")
    stat = input("Pick the stat: Magic, Cunning, Courage, Wisdom, Temper\n>")
    return stat

def playGame(player_character, computer_character, stat):
    player_stat = player_character[stat]
    computer_stat = computer_character[stat]

    print(f"Player {stat}: {player_stat}")
    print(f"AI {stat}: {computer_stat}")

    if player_stat > computer_stat:
        print("Player Wins")
    elif player_stat < computer_stat:
        print("AI Wins")
    else:
        print("It's a tie!")


printList()
choice = pickCharacter()
player_character, computer_character = extraSetup(choice)
stat = pickCategory()
playGame(player_character, computer_character, stat)