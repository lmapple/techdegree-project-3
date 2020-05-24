# techdegree-project-3
 Phrase Hunter

This is a word guessing game. It will select a phrase at random. This will be hidden from the
player. The player inputs individual characters to guess the phrase.



Reviewer Notes:

I am going for an Exceeds Expectations grade on this project.

Game initialization - Since the player will only guess one phrase per game, I opted not to create
a list of five Phrase objects per game. Instead I create one relevant instance of a randomly-selected
phrase.

OOP Principles - Once a player selects the option to play the game, an instance is created and the
method to start the game is called. I am considering the menu, adding a phrase to the text file,
and exiting the menu as being separate from running the game itself.



Treehouse Instructions:

Create a word guessing game: "Phrase Hunter." You’ll use Python and OOP (Object-Oriented Programming)
approaches to select a phrase at random, hidden from the player. A player tries to guess the phrase
by inputting individual characters.

Flow of the game

Using Python, you’ll create two Python classes with specific attributes and methods.
You'll create a Game class for managing the game, and a Phrase class to help with
storing attributes of a phrase with specific methods to help determine how to display
the phrase in the game.

Your code will choose a random phrase and use some logic you will implement to display
each letter of the phrase as underscore character placeholders, _.

Each time the player guesses a letter, the program compares the letter the player has
chosen with the random phrase. If the letter is in the phrase, the phrase object is
updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess the phrase (and win), or make five
incorrect guesses (and lose).

If the player completes the phrase before they run out of guesses, a winning screen appears.
If the player guesses incorrectly five times, a losing screen appears.

A player can guess a letter only once. After they’ve guessed a letter, your programming logic
will need to prevent that letter from being guessed a 2nd time.

After building this project, you'll have another great portfolio piece to show off your skills,
a fun app that you can share with your friends and family, and a good understanding of the
principles of Object-Oriented Programming.

Extended Instructions:

This game will be entirely console/terminal based.

The player’s goal is to guess all the letters in a hidden, random phrase. At the beginning of the
game, the player only sees the number of letters and words in the phrase, represented by an underscore
character _ as a placeholder on the screen for a given letter for that phrase.

The player inputs a guess for a letter in the phrase.

Once a correct letter is guessed, a player cannot guess that letter again.

If the guessed letter is in the phrase at least once, the phrase will replace all positions showing the
underscore _ with the appropriate letter. All occurrences of that letter are made visible (so if there
are 3 A's, all of the A's in the phrase appear at once).

If the selected letter is not in the phrase, the player loses a "life" (the player only has a limited
number of "lives").

The player keeps choosing letters until they reveal all the letters in the phrase, or until they make
five incorrect guesses.