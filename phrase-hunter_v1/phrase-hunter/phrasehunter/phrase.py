# Creates Phrase class to handle creation of phrases.


class Phrase():

  def __init__(self, phrase):

    from phrasehunter.character import Character

    # Players will only be allowed to guess a letter.
    self.valid_guesses = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z']
    self.length = int(len(phrase))
    self.incorrect_count = int(0)
    self.collection = []
    self.collection_names = []
    self.all_guesses = []

    # The Phrase instance will consist of a list of Character instances.
    for char in phrase:
      self.collection_names.append(str(char).lower())
      char = Character(char)
      self.collection.append(char)

    # Since spaces are counted as an automatic guess, these should be included
    # in the correct_count attribute.
    self.correct_count = (int(0)) + self.collection_names.count(" ")

  def check_guess(self,guess):

    # One letter can be guessed at a time.
    if len(guess) == 1 and str(guess).lower() in self.valid_guesses:

      # Each letter can only be guessed once.
      if str(guess).lower() in self.all_guesses:
        print('{} has already been guessed. Please try again.'.format(str(guess)))
      else:
        self.all_guesses.append(str(guess).lower())

        #Check to see if this is a correct or incorrect guess.
        if str(guess).lower() in self.collection_names:
          self.correct_count += self.collection_names.count(str(guess.lower()))

          # If guess is correct, redisplay the updated phrase.
          for char in self.collection:
            char.update(guess)
            print(char.show(), end = " ")
          print("\n")
        else:
          self.incorrect_count += 1

          # If guess is incorrect, display number of incorrect guesses.
          print('Incorrect Guesses: ' + str(self.incorrect_count))
          print('Remaining Chances: ' + str(5-self.incorrect_count))
    else:
      print('Your guess should consist of one letter. Please try again.')