def get_array(file_name: str):
    with open(file_name) as f:
        array = [[x for x in line.split()] for line in f]
    return(array)

def pokerhand(cards:list):
    faces = {
        "k" : 13
        "Q" : 12
        "J" : 11
        "T" : 10
    }
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0] # number of each card
    score = [0,0] #value of score and high card in hand

    for hand in range(0,5):
        if hand[0] in faces:
            count[faces[hand[0]]-1] += 1
        else:
            count[hand[0]-1] += 1

    #
    for i in range(13):
        if 



def poker_win(arr: list):
    '''find the maximum base exponent pair in array
    array is a list of lists
    '''
    count = 0
    for hand in arr:
        p1 = hand[:5]#splits into players
        p2 = hand[5:]

        score1 = pokerhand(p1)
        score2 = pokerhand(p2)

        if score1[0] > score2[0] or score1[0] == score2[0] and score1[1] > score2[1]: 
            count+=1 #if score1 pattern is better or if the patterns are equal and p1's cards are better
        elif score1[0] == score2[0] and score1[1] == score2[1]: 
            for card in high_cards
    return count

if __name__ == "__main__":
    exponents = get_array('p054_poker.txt')
    for row in exponents:
        print(row)