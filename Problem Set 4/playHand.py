def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    score = 0
    characters = n
    while characters > 0:
    
        # Display the hand
        print "Current Hand:",
        for letter in hand.keys():
            for j in range(hand[letter]):
                print letter,              # print all on the same line
        print
        
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        
        if word == ".":
            # End the game (break out of the loop)
            break
        else:
            if not isValidWord(word, hand, wordList):
                print "Invalid word, please try again. \n"
                # Reject invalid word (print a message followed by a blank line)
            else:
                points = getWordScore(word, n)
                characters -= len(word)
                print '"' + word + '"' + " earned " + str(points) + " points.",
                score += points
                print "Total score: " + str(score) + " points.\n"
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, word)
                # Update the hand 
           
    if characters == 0:                              
        print "Run out of letters. Total score: " + str(score) + " points."
    else:
        print "Goodbye! Total score: " + str(score) + " points."

