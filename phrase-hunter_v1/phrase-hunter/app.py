#Manages the menu, including adding phrases, starting the game, and exiting.


# Dunder Main statement.
if __name__ == '__main__':

  # Import Game class, regular expressions, and random.
  import re
  from phrasehunter.game import Game

  print('Welcome to Guess-That-Phrase. You are currently in the menu. What would you'
        ' like to do?')

  # Player should select a valid option from the menu.
  while True:
    player_input = input('(P)lay the game, (A)dd a phrase, or (E)xit   ')

    if player_input.upper() == 'P':

      # Create an instance of Game class.
      # Start the game.
      active_game = Game()
      try:
        active_game.start_game(active_game.current_phrase)
      except AttributeError:
        pass

      continue

    # Allow player to add their own phrases to the master phrase list.
    elif player_input.upper() == 'A':
      phrase_to_add = str(input('Please type the phrase you would like to add.   '))

      # Check to make sure that only letters can be added as a phrase.
      if re.search(r'[\w ]+[^\n\d_]',phrase_to_add):

        # Check to make sure phrase isn't blank.
        if len(phrase_to_add) != 0:
          with open("phrasehunter/phrase_master_list.txt","a") as open_file:
            open_file.write(phrase_to_add + "\n")
        else:
            print("Phrase must be at least one character. Phrase not added.")
      else:
        print('Phrase must contain letters only. No phrase added.')

      continue

    elif player_input.upper() == 'E':
      input('Goodbye. Have a great day.')
      break

    else:
      player_input = print('Invalid choice. Please try again.')
      continue