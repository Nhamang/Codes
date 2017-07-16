p1Deck = "5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 3 13 6 1 8 1".split()
p2Deck = "9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5".split()

#p1Deck = "3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1".split()
#p2Deck = "9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5".split()

#p1Deck = "1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13".split()
#p2Deck = "1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13".split()

def isEmpty(lst1):
    return (len(lst1) == 0)

def startRound():
    if(isEmpty(p1Deck) and isEmpty(p2Deck)):
        return 0
    elif(not isEmpty(p1Deck) and isEmpty(p2Deck)):
        return 1
    elif(isEmpty(p1Deck) and  not isEmpty(p2Deck)):
        return 2

    p1Card = int(p1Deck.pop(0))
    p2Card = int(p2Deck.pop(0))

    if(p1Card > p2Card):
        p1Deck.append(p1Card)
        p1Deck.append(p2Card)
    elif(p1Card < p2Card):
        p2Deck.append(p2Card)
        p2Deck.append(p1Card)
    else:
        outcome = cardWar(p1Card, p2Card)

    return(startRound())

def cardWar(p1Start, p2Start):
    p1War = []
    p2War = []

    if(isEmpty(p1Deck) and isEmpty(p2Deck)):
        return -1
    elif(not isEmpty(p1Deck) and isEmpty(p2Deck)):

        p1Deck.append(p1Start)
        for i in range(0, len(p1War)-1):
            p1Deck.append(p1War.pop(0))

        p1Deck.append(p2Start)
        for i in range(0, len(p2War)-1):
            p1Deck.append(p2War.pop(0))

        return -1
    elif(isEmpty(p1Deck) and not isEmpty(p2Deck)):
        p2Deck.append(p2Start)
        for i in range(0, len(p2War)-1):
            p2Deck.append(p2War.pop(0))

        p2Deck.append(p1start)
        for i in range(0, len(p1War)-1):
            p2Deck.append(p1War.pop(0))
        return -1

    for i in range(0, 4):
        if(isEmpty(p1Deck) or isEmpty(p2Deck)):
            break

        p1War.append(p1Deck.pop(0))
        p2War.append(p2Deck.pop(0))


    p1LastCard = p1War.pop(len(p1War)-1)
    p2LastCard = p2War.pop(len(p2War)-1)

    if(p1LastCard > p2LastCard):
        for i in p1War:
            p1Deck.append(p1War.pop(0))
        p1Deck.append(p1LastCard)

        for i in p2War:
            p1Deck.append(p2War.pop(0))
        p1Deck.append(p2LastCard)
        return 1
    elif(p1LastCard < p2LastCard):
        for i in p2War:
            p2Deck.append(p2War.pop(0))
        p2Deck.append(p2LastCard)

        for i in p1War:
            p2Deck.append(p1War.pop(0))
        p2Deck.append(p1LastCard)
        return 2
    else:
        outcome = cardWar(p1LastCard, p2LastCard)
        if(outcome == 1):
            p1Deck.append(p1Start)
            p1Deck.append(p2Start)
            return 1
        elif(outcome == 2):
            p2Deck.append(p2Start)
            p2Deck.append(p1Start)
            return 2
    return -1

print startRound()
