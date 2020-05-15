print("hello world")
def get_array(file_name: str):
    with open(file_name) as f:
        array = [[x for x in line.split()] for line in f]
    return(array)

def card_to_tuple(card: str):
    faces = {
            "A" : 14,
            "K" : 13,
            "Q" : 12,
            "J" : 11,
            "T" : 10,
            "9" : 9,
            "8" : 8,
            "7" : 7,
            "6" : 6,
            "5" : 5,
            "4" : 4,
            "3" : 3,
            "2" : 2,
        }
    return (faces[card[0]],card[1])

def check_flush(cards:list):
    for i in range(1,5): #checks all suits are the same as cards[1]
        if cards[i][1] != cards[1][1]:
            return False
    return True

def check_straight(cards:list):
    for i in range(1,5):
        if cards[i][0] != cards[i-1][0] + 1:
            return False
    return True

def sort_cards(cards): #NEED TO TEST ------------------------------------------------
    '''selection sort. Smallest to largest'''
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i][0] > cards[j][0]:
                cards[j],cards[i] = cards[i],cards[j]
    return cards

def remove_all(cards, removes: list):
    new = cards[:]
    for i in cards:
        if i[0] in removes:
            new.remove(i)
    return new

def pokerhand(cards:list):
    '''Returns the rating a list: [pokerhand rating, level of hand, highcard1, ...]'''
    for i in range(5):
        cards[i] = card_to_tuple(cards[i])
    cards = sort_cards(cards)
    
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0] # number of each card
    for card in cards:
        counts[card[0]-2] += 1

    if check_flush(cards):
        if check_straight(cards): 
            if cards[4][0] == 14: #royal flush
                return [10]
            else:
                return [9, cards[4]] #straight flush
        elif not (4 in counts or 3 in counts and 2 in counts): #Not a 4 of a kind or full house
            return [6] + cards[::-1] # flush
    
    if 4 in counts: #4 of a kind
        return [8] + [counts.index(4)+2, counts.index(1)+2]

    if 3 in counts and 2 in counts: # full house
            return[7] + [counts.index(3)+2, counts.index(2)+2]

    if check_straight(cards):
        return [5, cards[4]]

    if 3 in counts: #3 of a kind
        three = counts.index(3)+2
        return [4] + [three] + [x[0] for x in remove_all(cards, [three])][::-1]
    
    if counts.count(2) == 2: #two pair
        twos = []
        for i in range(len(counts)):
            if counts[i] == 2:
                twos.append(i + 2)
        return [3] + twos[::-1] + [x[0] for x in remove_all(cards, twos)][::-1]

    elif counts.count(2) == 1: # pair
        two = counts.index(2)+2
        return [2] + [two] + [x[0] for x in remove_all(cards, [two])][::-1]
    return [1] + [x[0] for x in cards][::-1] #high cards

def poker_win(arr:list):
    '''find the maximum base exponent pair in array
    array is a list of lists
    '''
    count = 1
    for hand in arr:
        p1 = hand[:5]#splits into players
        p2 = hand[5:]

        score1 = pokerhand(p1)
        score2 = pokerhand(p2)
        for i in range(5):
            if score1[i] > score2[i]:
                count += 1
                break
            if score1[i] < score2[i]:
                break
    return count

if __name__ == "__main__":
    hands = get_array('p054_poker.txt')
    print(poker_win(hands))
    