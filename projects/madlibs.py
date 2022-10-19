# According to Wikipedia, Mad Libs is a phrasal template word game, usually played at parties, 
# where one player prompts other players for a list of words to substitute blanks in a story 
# before reading out the completed story aloud. Source: https://en.wikipedia.org/wiki/Mad_Libs
 
# Example:
# We start with a story, containing several blanked out words. Here’s a basic example:
# Rumble in the  _______.
# We then prompt the user to fill in the gaps, in this case, with a noun or place. We might end up with something like this:
# Rumble in the Toilet.
# Obviously, the more entertaining the original story, the better the laughs will be at the end!

import os
### FUNCTIONS ###

# Display a title bar.
def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  Welcome to Mad Libs Games by FWCoder  ***")
    print("\t**********************************************")

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
choice = ''
while choice != 'q':    
    display_title_bar()
    
    # Let users know what they can do.
    print("\n[1] Start the game.")
    print("[q] Quit.")
    
    choice = input("What would you like to do? ")

    if choice == "q":
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")
    



