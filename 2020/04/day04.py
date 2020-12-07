"""
https://adventofcode.com/2020/day/4
"""
import itertools as it

passports = []
passports.append({"cid":" "}) # add this as it's optional anyway and adds new item to list
passport_count = 0
##lines = open("input.txt", "rb").read().splitlines()

# refactored using it.groupby tip from @eumiro
for is_not_empty, lines in it.groupby(open("input.txt"), lambda line: bool(line.strip())):
    if is_not_empty:
        pairs_list = map(lambda a: {a[0]:a[1]}, (split_line.split(':') for line in lines for split_line in line.split()))
        pairs_dict = {k: v for pair in pairs_list for k, v in pair.items()}
        if 'cid' not in pairs_dict: pairs_dict.update({'cid':''})
        passports.append(pairs_dict)

# Part 1

valid = 0
for passport in passports:
    if len(passport) == 8: valid +=1

print "Valid passports (Part 1): ",valid

# Part 2

cols= ['amb','blu','brn','gry','grn','hzl','oth']

valid = 0
for passport in passports:
    is_valid = True

    if len(passport) < 8:
        is_valid = False

    if 'byr' in passport:
        byr = int(passport['byr'])
        if byr < 1920 or byr > 2002:
            is_valid = False
    else:
        is_valid = False

    if 'iyr' in passport:
        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            is_valid = False
    else:
        is_valid = False

    if 'eyr' in passport:
        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            is_valid = False
    else:
        is_valid = False

    if 'hgt' in passport:
        try:
            a = int(passport['hgt'][:-2])
        except:
            is_valid = False
        b = passport['hgt'][-2:]
        if not (b == 'cm' or b == 'in'):
            is_valid = False
        else:
            if b == 'cm':
                if a <150 or a>193:
                    is_valid= False
            if b == 'in':
                if a <59 or a>76:
                    is_valid = False

    else:
        is_valid = False

    if 'hcl' in passport:
        hcl = passport['hcl']
        if hcl[0] != '#':
            is_valid = False
        a = hcl[1:] 
        if len(a) != 6:
            is_valid = False
        try:
            b = int(a,16)
        except:
            is_valid = False
    else:
        is_valid = False

    if 'ecl' in passport:
         if passport['ecl'] not in cols:
             is_valid = False
    else:
        is_valid = False

    if 'pid' in passport:
        pid = passport['pid'] 
        if len(pid) != 9:
            is_valid = False
        try:
            int(pid)
        except:
            is_valid = False
    else:
        is_valid = False
   
    if is_valid == True:
        valid += 1
              

print "Valid passports (Part 2): ", valid
