
'''
 Author:  Kenneth lin
 Date:    10/30/2019
 Prog:    Blackjack.py
 Descr:   Simulate a blackjack game between 2 player
'''

import random as R

def createDeck():
    # create a dictionary with each card and its value
    # stored as key-value pairs
    deckOfCards = {'Ace of Spades' :1, '2 of Spades' :2, '3 of Spades' :3,
                   '4 of Spades' :4, '5 of Spades' :5, '6 of Spades' :6,
                   '7 of Spades' :7, '8 of Spades' :8, '9 of Spades' :9,
                   '10 of Spades' :10, 'Jack of Spades' :10,
                   'Queen of Spades' :10, 'King of Spades': 10,

                   'Ace of Hearts' :1, '2 of Hearts' :2, '3 of Hearts' :3,
                   '4 of Hearts' :4, '5 of Hearts' :5, '6 of Hearts' :6,
                   '7 of Hearts' :7, '8 of Hearts' :8, '9 of Hearts' :9,
                   '10 of Hearts' :10, 'Jack of Hearts' :10,
                   'Queen of Hearts' :10, 'King of Hearts': 10,

                   'Ace of Clubs' :1, '2 of Clubs' :2, '3 of Clubs' :3,
                   '4 of Clubs' :4, '5 of Clubs' :5, '6 of Clubs' :6,
                   '7 of Clubs' :7, '8 of Clubs' :8, '9 of Clubs' :9,
                   '10 of Clubs' :10, 'Jack of Clubs' :10,
                   'Queen of Clubs' :10, 'King of Clubs': 10,

                   'Ace of Diamonds' :1, '2 of Diamonds' :2, '3 of Diamonds' :3,
                   '4 of Diamonds' :4, '5 of Diamonds' :5, '6 of Diamonds' :6,
                   '7 of Diamonds' :7, '8 of Diamonds' :8, '9 of Diamonds' :9,
                   '10 of Diamonds' :10, 'Jack of Diamonds' :10,
                   'Queen of Diamonds' :10, 'King of Diamonds': 10}

    # return the deck of cards
    return deckOfCards

def getRandCard(fullDeck):

    # Separate a deck of cards by card, card value and return full deck
    keyList = list(fullDeck)

    # randomly select each card and value
    randIndex = R.randint(0, len(fullDeck) - 1)
    card = keyList[randIndex]
    cardValue = fullDeck.pop(card, 'NOT FOUND')

    return card, cardValue, fullDeck


def dealRandCard(hand):
    # Initialize all variables needed
    roundPlayed = 0
    cardPlayed = 0
    player2Win = 0
    player1Win = 0

    # try the commands below
    try:
        # do until there are still cards in the deck
        while len(hand) > 0:
            # initialize variables
            player1 = 0
            player2 = 0
            roundPlayed += 1
            dealNum = 1

            # display column/lable header
            print('**NEW ROUND**')
            print(format('Deal', '>10s'), format('Player 1', '>15s'), format('Player 2', '>25s'))
            print(format('----', '>10s'), format('--------', '>15s'), format('--------', '>25s'))

            # deal cards when player1 and player2 are under 21 points
            while player1 < 21 and player2 < 21 and len(hand) >= 2:

                # randomly select card and value from deck for player1
                card, value = R.choice(list(hand.items()))
                hand.pop(card)  # once selected, discard the card

                player1 += value  # player1 points plus the value of card

                # display number of deals and player1 card
                print(format(dealNum, '>10d'),  end='')
                print(format(card, '>20s'), end='')

                # count number of deals and cards that have been played
                dealNum += 1
                cardPlayed += 2

                # if either player draws an Ace, then determine wheter the ACe is 1 or 11
                if card == 'Ace of Spades' or card == 'Ace of Clubs' or card == 'Ace of Diamonds' \
                        or card == 'Ace of Hearts':
                    if player1 + value < 21:
                        value += 10
                    else:
                        value += 1

                # randomly select card and value from deck for player2
                card, value = R.choice(list(hand.items()))
                hand.pop(card)
                player2 += value

                # display the card
                print(format(card, '>25s'))

                # if player2 draws an Ace, determine whether the Ace is 1 or 11
                if card == 'Ace of Spades' or card == 'Ace of Clubs' or card == 'Ace of Diamonds' \
                        or card == 'Ace of Hearts':
                    if player2 + value < 21:
                        value += 10
                    else:
                        value += 1

                # This counts the number of wins player1 and player2 has
                if player1 > 21 and player2 <= 21:
                    player2Win += 1
                elif player2 > 21 and player1 <= 21:
                    player1Win += 1
                elif player1 == 21 and player2 != 21:
                    player1Win += 1
                elif player2 == 21 and player1 != 21:
                    player2Win += 1

                print()

            # display lablels and player1/player2 score, and the winner of each round
            print('==========', end='')
            print(format('==============', '>20s'), format('==============', '>25s'))

            print('Hand Value', end='')
            print(format(player1, '>15d'), format(player2, '>25d'))
            print()
            # Call the determine winner procedure
            determineWin(player1, player2)
            print()
            print()
            print()
            print()

        # game summary statistic that totals all player1/player2 wins and # rounds player
        print('**SUMMARY GAME STATISTICS**')
        print(format('Rounds played', '<30s'), roundPlayed)
        print(format('Cards Played', '<30s'), cardPlayed)
        print(format('Player 1 wins', '<30s'), player1Win)
        print(format('Player 2 wins', '<30s'), player2Win)

    except:
        pass  # if there is a sequence error, let it pass

# procedure that determines who is the winner
def determineWin(player1, player2):

    # this procedure will display who the winner is when called upon
    if player1 > 21 and player2 > 21:
        print('There is no winner')
    elif player1 > 21:
        print('Player 2 wins')
    elif player2 > 21:
        print('Player 1 wins')
    elif player1 == 21 and player2 != 21:
        print('Player 1 wins')
    elif player2 == 21 and player1 != 21:
        print('Player 2 wins')
    elif player1 == 21 and player2 == 21:
        print('There is no winner')


def main():

    fullDeck = createDeck()  # make fulldeck equal to the deck of cards
    hand = {}  # set hand to equal dictionary

    # for loop that iterates 52 times
    for counter in range(0, len(fullDeck)):
        # get card, value and eck from getRandCard function
        card, value, deck = getRandCard(fullDeck)
        # set hand dictionary to the full deck of cards
        hand[card] = value

    # deal card/display results procedure
    dealRandCard(hand)


main()