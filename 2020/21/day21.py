"""
https://adventofcode.com/2020/day/16
"""

#code = map(lambda a: [a[0],int(a[1])],(x.split() for x in open("input.txt", "rb").read().splitlines()))
lines = open("input.txt", "rb").read().splitlines()

data= []
allergens = {}
ingredients = {}
allergen_list = {}
def load_data():
    global data,ingredients,allergens
    for line in lines:
        parts = line.split('(')
        i_list= parts[0].split()
        a_str = parts[1][:-1].replace(',','')
        a_list = a_str.split()[1:]
        data.append([i_list,a_list])

        for a in a_list:
            if a not in allergens:
                allergens[a] = []
            for i in i_list:
                allergens[a].append(i)

        for i in i_list:
            if i not in ingredients:
                ingredients[i] = []
            for a in a_list:
                ingredients[i].append(a)                

load_data()

def part1():
    global allergen_list

    # find overlaps in allregens ingredients lists
    # so first build lists
    for allergen in allergens:
        allergen_list[allergen] = []
        for i,a in data:
            if allergen in a:
                allergen_list[allergen].append(i)

    # then remove so only items that appear in all lists remain
    for a,i_list in allergen_list.items():
        allergen_list[a] = list(set(i_list[0]).intersection(*i_list))
    used = []
    for a,i_list in allergen_list.items():
        for i in i_list:
            if i not in used: used.append(i)

    # now find ingredients that arn't in above list
    count = 0
    for i in ingredients:
        if i not in used:
            count += sum(a.count(i) for a,b in data)
        
    return count

print "Part 1 answer:",part1()

def part2():
    final_list = []
    removed = True
    while removed == True:
        removed = False
        # build dict using single entries
        for a,i_list in allergen_list.items():
            if len(i_list) == 1:
                final_list.append([a,i_list[0]])
                removed = True
        # remove double ent
        for [a,ingredient] in final_list:
            for allergen,i_list in allergen_list.items():
                if ingredient in i_list:
                    i_list.remove(ingredient)
                    removed = True

    final_list.sort()
    return ','.join([b for [a,b] in final_list])

print "Part 1 answer",part2()

