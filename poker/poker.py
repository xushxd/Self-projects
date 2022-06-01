from collections import Counter
import time
start_time = time.perf_counter ()

d = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def high_hand():# 1
    max = l[0]
    pos = 0
    for i in range(len(l)):
        if l[i]>max: max = l[i];pos = i
    if l.count(max) > 1: return "Dead Heat" \
                                "" # ничья
    return ('P2 1' if pos > 4 else 'P1 1')

def one_pair():# 2
    winner = 0
    if ['True' for k, v in Counter(l[:5]).items() if v == 2] == ['True']: winner += 1
    if ['True' for k, v in Counter(l[5:]).items() if v == 2] == ['True']: winner += 2
    if winner == 1: return 'P1 2'
    elif winner == 2: return 'P2 2'
    elif winner == 3: # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items() if v == 2])
        p2 = sum([k for k, v in Counter(l[5:]).items() if v == 2])
        if p1 > p2: return 'P1 2'
        elif p1 == p2: return high_hand()
        else : return 'P2 2'
    return high_hand()

def two_pairs():# 3
    winner = 0
    if ['True' for k, v in Counter(l[:5]).items() if v == 2] == ['True', 'True']: winner += 1
    if ['True' for k, v in Counter(l[5:]).items() if v == 2] == ['True', 'True']: winner += 2
    if winner == 1: return 'P1 3'
    elif winner == 2: return 'P2 3'
    elif winner == 3: # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2: return 'P1 3'
        elif p1 == p2: return one_pair()
        else: return 'P2 3'
    return one_pair()

def three_of_a_kind():# 4
    winner = 0
    if ['True' for k, v in Counter(l[:5]).items() if v == 3] == ['True']: winner += 1
    if ['True' for k, v in Counter(l[5:]).items() if v == 3] == ['True']: winner += 2
    if winner == 1: return 'P1 4'
    elif winner == 2: return 'P2 4'
    elif winner == 3: # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2: return 'P1 4'
        elif p1 == p2: return two_pairs()
        else: return 'P2 4'
    return two_pairs()

def straight():# 5
    winner = 0
    x = -3
    n = 1
    for i in l[:4]:
        if i == l[n] - 1:
            x += 1
        n += 1
    if x == 1: winner += 1

    x = -3
    n = 6
    for i in l[5:9]:
        if i == l[n] - 1:
            x += 1
        n += 1
    if x == 1: winner += 2

    if winner == 1:
        return 'P1 5'
    elif winner == 2:
        return 'P2 5'
    elif winner == 3:  # если ничья, вернуть игрока с большей рукой
        p1 = sum(l[:4])
        p2 = sum(l[5:9])
        if p1 > p2:
            return 'P1 5'
        elif p1 == p2:
            return three_of_a_kind()
        else:
            return 'P2 5'
    return three_of_a_kind()

def flush():# 6
    winner = 0
    if ['True' for k, v in Counter(m[:5]).items() if v == 5] == ['True']: winner += 1
    if ['True' for k, v in Counter(m[5:]).items() if v == 5] == ['True']: winner += 2
    if winner == 1: return 'P1 6'
    elif winner == 2: return 'P2 6'
    elif winner == 3: # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2: return 'P1 6'
        elif p1 == p2: return straight()
        else: return 'P2 6'
    return straight()

def full_house():# 7
    winner = 0
    if ['True' for k, v in Counter(l[:5]).items() if v == 3] == ['True'] and \
            ['True' for k, v in Counter(l[:5]).items() if v == 2] == ['True']: winner += 1
    if ['True' for k, v in Counter(l[5:]).items() if v == 3] == ['True'] and \
            ['True' for k, v in Counter(l[5:]).items() if v == 2] == ['True']: winner += 2
    if winner == 1:
        return 'P1 7'
    elif winner == 2:
        return 'P2 7'
    elif winner == 3:  # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2:
            return 'P1 7'
        elif p1 == p2:
            return flush()
        else:
            return 'P2 7'
    return flush()

def four_of_a_kind():# 8
    winner = 0
    if ['True' for k, v in Counter(l[:5]).items() if v == 4] == ['True']: winner += 1
    if ['True' for k, v in Counter(l[5:]).items() if v == 4] == ['True']: winner += 2
    if winner == 1: return 'P1 8'
    elif winner == 2: return 'P2 8'
    elif winner == 3: # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2: return 'P1 8'
        elif p1 == p2: return full_house()
        else: return 'P2 8'
    return full_house()

def straight_flush():# 9
    winner = 0
    x = -3
    n = 1
    for i in l[:4]:
        if i == l[n] - 1:
            x += 1
        n += 1
    if x == 1 and \
            ['True' for k, v in Counter(m[:5]).items() if v == 5] == ['True']: winner += 1

    x = -3
    n = 6
    for i in l[5:9]:
        if i == l[n] - 1:
            x += 1
        n += 1
    if x == 1 and \
            ['True' for k, v in Counter(m[5:]).items() if v == 5] == ['True']: winner += 2

    if winner == 1:
        return 'P1 9'
    elif winner == 2:
        return 'P2 9'
    elif winner == 3:  # если ничья, вернуть игрока с большей рукой
        p1 = sum(l[:4])
        p2 = sum(l[5:9])
        if p1 > p2:
            return 'P1 9'
        elif p1 == p2:
            return four_of_a_kind()
        else:
            return 'P2 9'
    return four_of_a_kind()

def royal_flush():# 10
    winner = 0
    if 10 in l[:5] and 11 in l[:5] and 12 in l[:5] and 13 in l[:5] and 14 in l[:5] and \
            ['True' for k, v in Counter(m[:5]).items() if v == 5] == ['True']: winner += 1
    if 10 in l[5:] and 11 in l[5:] and 12 in l[5:] and 13 in l[5:] and 14 in l[5:] and \
            ['True' for k, v in Counter(m[5:]).items() if v == 5] == ['True']: winner += 2
    if winner == 1:
        return 'P1 10'
    elif winner == 2:
        return 'P2 10'
    elif winner == 3:  # если ничья, вернуть игрока с большей рукой
        p1 = sum([k for k, v in Counter(l[:5]).items()])
        p2 = sum([k for k, v in Counter(l[5:]).items()])
        if p1 > p2:
            return 'P1 10'
        elif p1 == p2:
            return straight_flush()
        else:
            return 'P2 10'
    return straight_flush()

f = open('p054_poker.txt')
two_hands = f.read().strip().split('\n')
f.close()

player1swins = 0

for j in two_hands:
    l = [d[i[0]] for i in j.split()]
    m = [i[1] for i in j.split()]
    if royal_flush()[1] == '1':
        player1swins += 1

print(player1swins)

print('     ', round(time.perf_counter () - start_time, 13), "seconds")
