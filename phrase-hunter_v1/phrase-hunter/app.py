# Dunder Main statement.
if __name__ == '__main__':

  # Import Game class, regular expressions, and random.
  from phrasehunter.game import Game
  import re, random

  print('Welcome to Guess-That-Phrase. You are currently in the menu. What would you like to do?')

  while True:
    player_input = input('(P)lay the game, (A)dd a phrase, or (E)xit   ')

    if player_input.upper() == 'P':

      with open("phrasehunter/phrase_master_list.txt") as open_file:
        data = open_file.read()

#!! Add error handling here in case text file is blank
      random_phrase = random.choice(re.findall(r'[\w ]+[^\n]',data))

      # Inside Dunder Main:
      ## Create an instance of your Game class
      ## Start your game by calling the instance method that starts the game loop

      active_game = Game(random_phrase)
      active_game.start_game()

      continue

    #Allow player to add their own phrases to the master phrase list.
    elif player_input.upper() == 'A':
      phrase_to_add = str(input('Please type the phrase you would like to add.   '))
      if len(phrase_to_add) != 0:
          with open("phrasehunter/phrase_master_list.txt","a") as open_file:
            open_file.write(phrase_to_add + "\n")
      else:
          print("Phrase must be at least one character. Phrase not added.")

      continue

    elif player_input.upper() == 'E':
      input('Goodbye. Have a great day.')
      break

    else:
      player_input = print('Invalid choice. Please try again.')
      continue



