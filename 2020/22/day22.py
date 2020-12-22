"""
https://adventofcode.com/2020/day/22
"""
lines = open("input.txt", "rb").read().splitlines()

deck = [[],[]]

def load_data():
    global deck
    section = -1
    for line in lines:
        if 'Player' in line:
            section+=1      
        elif line != '':
            deck[section].append(int(line))      

load_data()

def part1(deck1, deck2):

    while len(deck1) > 0 and len(deck2) > 0:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        else:
            deck2.append(c2)
            deck2.append(c1)

    win = 1 if len(deck1) > 0 else 0

    count = 0
    for n,v in enumerate(deck[1-win]):
        count += (len(deck[1-win])-n)*v

    return count

print "Part 1 answer:",part1(deck[0],deck[1])
deck = [[],[]]
load_data()

def play_round(deck1,deck2):
    hashes = []

    while len(deck1) > 0 and len(deck2) > 0:
        new_hash = hash(tuple(deck1))
        if new_hash in hashes:
            return 1,0
        hashes.append(new_hash)

        d1 = deck1.pop(0)
        d2 = deck2.pop(0)

        if len(deck1) >= d1 and  len(deck2) >= d2:

            winner, score = play_round(list(deck1[:d1]),list(deck2[:d2]))
            if winner == 1:
                deck1.append(d1)
                deck1.append(d2)
            else:
                deck2.append(d2)
                deck2.append(d1)

        elif d1 > d2:
                deck1.append(d1)
                deck1.append(d2)
        else:
                deck2.append(d2)
                deck2.append(d1)

    d1s = 0
    for n,v in enumerate(deck1):
        d1s += (len(deck1)-n)*v
    d2s = 0
    for n,v in enumerate(deck2):
        d2s += (len(deck2)-n)*v
        
    winner = 1 if len(deck2) == 0 else 2
    score = d1s+d2s

    return winner, score

def part2(deck1, deck2):
    winner,score = play_round(deck1,deck2)
    return score


print "Part 2 answer:", part2(deck[0],deck[1])
