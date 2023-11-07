import random

# Points for each letter
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Letters available in the bag
bag = ["A"] * 9 + ["B"] * 2 + ["C"] * 2 + ["D"] * 4 + ["E"] * 12 + ["F"] * 2 + ["G"] * 3 + ["H"] * 2 + \
      ["I"] * 9 + ["J"] * 1 + ["K"] * 1 + ["L"] * 4 + ["M"] * 2 + ["N"] * 6 + ["O"] * 8 + ["P"] * 2 + \
      ["Q"] * 1 + ["R"] * 6 + ["S"] * 4 + ["T"] * 6 + ["U"] * 4 + ["V"] * 2 + ["W"] * 2 + ["X"] * 1 + \
      ["Y"] * 2 + ["Z"] * 1

def draw_tiles(num_tiles):
    """Draw a specified number of tiles from the bag."""
    tiles = random.sample(bag, num_tiles)
    for tile in tiles:
        bag.remove(tile)
    return tiles

def calculate_score(word):
    """Calculate the score of a given word based on the points list."""
    score = 0
    for letter in word:
        letter = letter.upper()
        if 'A' <= letter <= 'Z':
            score += points[ord(letter) - ord('A')]
    return score

def main():
    player_score = 0

    while True:
        num_tiles = int(input("Enter the number of tiles to draw (0 to quit): "))
        if num_tiles == 0:
            break

        tiles = draw_tiles(num_tiles)
        print(f"Your tiles: {', '.join(tiles)}")

        word = input("Enter a word: ").upper()

        if set(word).issubset(set(tiles)):
            score = calculate_score(word)
            player_score += score
            print(f"Score for '{word}': {score}")
            print(f"Total score: {player_score}")
        else:
            print("Invalid word. You don't have the required tiles.")

if __name__ == "__main__":
    main()
