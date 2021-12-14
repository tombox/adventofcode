"""
https://adventofcode.com/2021/day/14
"""

def load_data(filename: str) -> list:
    " Load data "
    lines = open(filename, "r").read().splitlines()
    data = {}
    for line in lines[2:]:
        d = line.split(' ')
        data[d[0]] = d[2]
    return lines[0],data


def part1(file: str) -> int:
    " Day 14 puzzle part 1"
    pt,pairs  = load_data(file)

    n = 0
    t2 = pt

    while n < 10:
        t1 = t2
        t2 = t1[0]
        for p in range(len(t1)-1):
            t2 += pairs[t1[p]+t1[p+1]] + t1[p+1]
        n+=1

    counts = {}
    for c in t2:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    return  counts[max(counts,key=counts.get)] - counts[min(counts,key=counts.get)]

def map_pairs(pairs):
    p = {}
    for k in pairs:
       p[k] = [k[0]+pairs[k],pairs[k]+k[1]]
    return p

def part2(file: str, loops=40) -> int:
    " Day 14 puzzle part 2"
    pt,pairs  = load_data(file)
    m = map_pairs(pairs)

    final_counts = {}
    for pos in range(len(pt)-1):
        this_pair = pt[pos]+ pt[pos+1]
        pair_counts = {}
        pair_counts[this_pair] = 1

        for n in range(loops):
            new_pair_counts = {}
            for pair in pair_counts:
                current_count = pair_counts[pair]
                pair1,pair2 = m[pair]

                if pair1 not in new_pair_counts:
                    new_pair_counts[pair1] = current_count
                else:
                    new_pair_counts[pair1] += current_count

                if pair2 not in new_pair_counts:
                    new_pair_counts[pair2] = current_count
                else:
                    new_pair_counts[pair2] += current_count

            pair_counts = new_pair_counts


        for pair in pair_counts:
            if not pair[0] in final_counts:
                final_counts[pair[0]] = pair_counts[pair]
            else:
                final_counts[pair[0]] += pair_counts[pair]  

            if not pair[1] in final_counts:
                final_counts[pair[1]] = pair_counts[pair]
            else:
                final_counts[pair[1]] += pair_counts[pair] 
    # remove duplicated values
    for c in final_counts:
        final_counts[c] = (final_counts[c]+1)//2

    max_count = final_counts[max(final_counts,key=final_counts.get)]
    min_count = final_counts[min(final_counts,key=final_counts.get)]

    return max_count - min_count


def test_example_part1():
    " Pytest for function example data part1() "
    assert part1("test-input.txt") == 1588

def test_part1():
    " Pytest for function part1() "
    assert part1("input.txt") == 3555

def test_example_part2():
    " Pytest for function example data part2() "
    assert part2("test-input.txt") == 2188189693529

def test_part2():
    " Pytest for function part2() "
    assert part2("input.txt") == 4439442043739

print("Part 1 test answer = ", part1("test-input.txt"))
print("Part 1 answer = ", part1("input.txt"))

print("Part 2 test answer = ", part2("test-input.txt"))
print("Part 2 answer = ", part2("input.txt"))

#print("Part 3 answer = ", part2("input.txt",40))