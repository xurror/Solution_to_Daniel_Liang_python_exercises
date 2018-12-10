import random
card = random.randint(1, 4)
rank = random.randint(1, 11)

##pick = eval(input("Enter a random number: "))
##
##pick = card

Ace = 'Ace'
Jack = 'Jack'
Queen = 'Queen'
King = 'King'
clubs = 'Clubs'
Diamonds = 'Diamonds'
Hearts = 'Hearts'
Spades = 'Spades'

if rank == 1:
    rank = Ace
elif rank == 2:
    rank = 2
elif rank == 3:
    rank = 3
elif rank == 4:
    rank = 4
elif rank == 5:
    rank = 5
elif rank == 6:
    rank = 6
elif rank == 7:
    rank = 7
elif rank == 8:
    rank = 8
elif rank == 9:
    rank = 9
elif rank == 10:
    rank = 10
elif rank == 11:
    rank = Jack
elif rank == 12:
    rank = King
elif rank == 13:
    rank = Queen

if card == 1:
    card = Clubs
elif card == 2:
    card = Diamonds
elif card == 3:
    card = Hearts
elif card == 4:
    card = Spades

print("The card you picked is the", rank, "of", card)
