# Creates Game class to handle starting the game, user interactions,
# getting a random phrase, checking for a win/loss state, and
# managing the turns of the player.


class Game():

  def __init__(self):
    import re,random
    from phrasehunter.phrase import Phrase

    with open("phrasehunter/phrase_master_list.txt") as open_file:
      data = open_file.read()

    # Ensure there is at least one valid phrase in phrase_master_list.txt.
    try:
      random_phrase = random.choice(re.findall(r'[\w ]+[^\n\d_]',data))
      self.current_phrase = Phrase(random_phrase)

    except IndexError as err:
      print("There are currently no saved phrases. Please add at least one valid"
            " phrase before playing the game.")

  def start_game(self,*args):
    print('Welcome to the Guess-That-Phrase! Guess the phrase to win!')

    # Display the initial phrase with hidden characters.
    for char in self.current_phrase.collection:
      print(char.show(), end = " ")
    print("\n")
    while self.current_phrase.correct_count < self.current_phrase.length and self.current_phrase.incorrect_count < int(5):

      # Collect user guesses.
      self.current_phrase.check_guess(input('What letter would you like to guess?   '))

    # If there are five incorrect guesses, the player loses.
    if self.current_phrase.incorrect_count == 5:
      print('Sorry, you lose. Only five incorrect guesses are allowed.')

    # If the player guesses all characters in the phrase, they win.
    elif self.current_phrase.correct_count == self.current_phrase.length:
      print('Congratulations! You guessed the phrase. You win.')
    print("Would you like to play again?")