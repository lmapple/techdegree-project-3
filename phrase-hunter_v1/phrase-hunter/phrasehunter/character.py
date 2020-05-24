# Creates Character class to help a Phrase determine how an individual
# character should display itself.

# Responsible for holding the state of a given single character.
class Character():

  def __init__(self, char):

    self.original = str(char)

    # If a character is a space, this counts as an automatic guess
    # and should always show.
    if self.original == " ":
      self.was_guessed = True
    else:
      self.was_guessed = False

  def update(self,guess):

    # If the guess character is an exact match to the original character,
    # update the state of the character.
    if str(guess).lower() == self.original.lower():
      self.was_guessed = True

  def show(self):

    # If the character has been guessed, the character should be displayed.
    # If the character has not been guessed, '_' should be displayed.
    if self.was_guessed == True:
      return self.original
    else:
      return '_'