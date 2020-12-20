"""
https://adventofcode.com/2020/day/15
"""

numbers = [0,14,1,3,7,9]
prev = now = turn_count = 0
turns = []

while turn_count < 2020:
    if turn_count < len(numbers):
        now = numbers[turn_count]
    elif turn_count == len(numbers):
        now = 0
    elif prev in turns[:-1]:
        turns.reverse()
        pos1 = turns.index(prev)
        pos2 = turns.index(prev,pos1+1)
        now = pos2-pos1
        turns.reverse()
    else:
        now = 0

    turns.append(now)
    prev = now
    turn_count += 1

print "Part 1 answer:",now

prev = now = turn_count = 0
cache1 = {}
cache2 = {}

while turn_count < 30000000:
    if turn_count < len(numbers):
        now = numbers[turn_count]
    elif turn_count == len(numbers):
        now = 0
    elif prev in cache2:
        now = cache1[prev] - cache2[prev]
    else:
        now = 0

    if now in cache1:
        cache2[now] = cache1[now]
    cache1[now] = turn_count

    turn_count += 1
    prev = now

print "Part 2 answer:", now
