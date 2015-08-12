# >>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# >>> displayHand(hand) # Implemented for you
# a q l l m u i
# >>> hand = updateHand(hand, 'quail') # You implement this function!
# >>> hand
# {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
# >>> displayHand(hand)
# l m  


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    frequencies = []
    for letter in hand.keys():
        frequencies.append(hand[letter])
    newHand = dict(zip(hand.keys(), frequencies))
    for letter in word:
        newHand[letter] = newHand.get(letter) - 1
    return newHand
