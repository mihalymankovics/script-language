from typing import List
import logging


def get_all_index(text: str, word: str) -> List[int]:
    if type(text) != str:
        raise TypeError
    if len(text) != 1:
        raise ValueError
    # return [i = i, letter in enumerate(word) if letter == text]
    found_index = []
    for i in range(len(word)):
        if word[i] == text:
            found_index.append(i)
    return found_index

# 1. l -> xxllx
# 2. e -> xellx


def get_new_masked_word(masked_word: str, word: str, indexes: List[int]):
    new_masked_word_list = list(masked_word)

    for step in range(len(word)):
        if step in indexes:
            new_masked_word_list[step] = word[step]

    return "".join(new_masked_word_list)


def lost():
    print("Sorry, U have lost")
    exit(1)


def win():
    print("Congratulations, U won")
    exit(0)


def new_guess(guess: str, word: str, masked_word: str):
    index_list = get_all_index(guess, word)
    return get_new_masked_word(masked_word, word, index_list)


def handle_final_guess(text: str, word: str):
    if text == word:
        win()
    else:
        lost()


if __name__ == "__main__":
    FORMAT = '%(asctime)s - %(levelname)s %(message)s'
    logging.basicConfig(filename='hangman.log', filenode='w', Level=logging.DEBUG)
    LOGGER = logging.getLogger()
    LOGGER.debug('Debug')
    LOGGER.info('Info')
    LOGGER.warning('Warning')
    LOGGER.error('Error')
    LOGGER.critical('Critical')

    word = "hello"
    MAX_GUESS = 3
    print(f"hangman application. Try to guess my word. You have {MAX_GUESS} chance.")

    guess_list = ['s', 'l', 'o', 'h']

    masked_word = len(word) * "x"

    for step in range(MAX_GUESS):
        print(f"{step + 1}, step, give me a letter")
        text = input()

        LOGGER.debug(f'Input: {text}, Step {step}')

        is_new_guess = len(text) == 1
        if is_new_guess:
            masked_word = new_guess(text, word, masked_word)
            print(f"masked word {masked_word}")
            if masked_word == word:
                LOGGER.info(f'Win')
                win()
        else:
            LOGGER.info(f'Final Guess: {text}')
            handle_final_guess(text, word)

    lost()
