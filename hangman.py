import random

guesses = 10

random_words = [
    "apple",
    "strawberry",
    "orange",
    "banana",
    "mango",
    "kiwi",
    "pineapple",
    "menlon",
    "watermelon",
    "cherry",
    "apricot",
    "plum",
]
replaced_word = []


def get_random_word(words):
    return random.choice(words)


def play_game(word):
    global guesses
    replaced_word = []
    guesses = 10
    for _ in enumerate(word):
        replaced_word.append("_")
    print(f"Try to guess the word by typing letters.")
    while guesses > 0 and "_" in replaced_word:
        print(f"\n There is {guesses} left. \n")

        for let in replaced_word:
            print(let, end="")

        guessed_letter = input("\n What's your guess? ")

        if guessed_letter in word:
            for i, letter in enumerate(word):
                if guessed_letter == letter:
                    replaced_word[i] = letter

        else:
            guesses -= 1
    if not "_" in replaced_word:
        print(
            """
        *********************************

        Congrats 🎉 you won! Would you like
        to play again? (y) or (any)

        *********************************        
        
        """
        )

        key = str(input(""))
        if key == "y" or key == "Y":
            main()
        else:
            exit(1)

    if guesses <= 0:
        print(
            """
    *********************************

    You Lost :( wanna play again? (y) or (any)


    *********************************        
    
    """
        )
        guess_key = str(input(""))
        if guess_key == "y" or guess_key == "Y":
            main()
        else:
            exit(1)


def main():
    print(
        f"""
    ---------------------------------------------------------\n
        Welcome to hangman game! You have to guess a few fruits here.
        You have {guesses} guesses.
    --------------------------------------------------------- \n
    """
    )
    selected_word = get_random_word(random_words)
    play_game(selected_word)


main()
