'''
основной файл принтэйбл дот работает отлично без никаких косяков
сегодня 08.06.22 и по моему я 5 день подряд пытаюсь доделать именно этот файл 
который отвечает за check_win в игре. я подза*бался и оставлю этот файл на потом
'''

'''
def dfs_mini(i, j, area, grey=None, black=None, iplus=1):
    if grey == None: grey = []
    if black == None: black = []
    i += iplus

    for row, col in [(0,1),(1,0),(0,-1),(-1,0)]:
        ni,nj = i+row, j+col

        if area[ni][nj] == area[i][j] and not (ni,nj) in grey and not (ni,nj) in black:
            grey.append((i,j))
            return dfs_mini(ni,nj, area, grey, black)
    else:
        if grey:
            last_grey = grey.pop()
            black.append((i,j))
            # area[i][j] = 'ob' # tut nado nayti player'a i sdelat 'wb' or 'wr'
            return dfs_mini(last_grey[0],last_grey[1],area,grey,black)
        else:
            black.append((i,j))
            # area[i][j] = 'ob'
            return black
'''


'''
def come_back(area,grey,i,j):
    '''
    comes back through grey points
    '''
    for k,n in enumerate(grey): 
        if n == (i,j):
            grey = grey[k:]
    print(grey)

    for i in grey:
        area[i[0]][i[1]] = 'ob'
    return area

def dfs(i, j, area, size, grey=None, black=None, route=None):
    if grey == None: grey = []
    if black == None: black = []
    if route == None: route = []
    print('--------------',i,j)

    for row, col in [(-1,1),(1,1),(0,1),(1,0),(1,-1),(-1,-1),(0,-1),(-1,0)]:
        ni,nj = i+row, j+col

        # if ni or nj are out of range
        if not ni >= 0 or not nj >= 0 or \
          ni > size or nj > size:
            continue

        if area[ni][nj] == area[i][j] and not (ni,nj) in grey and not (ni,nj) in black:
            grey.append((i,j))
            print(f'grey {i,j}\n')
            route.append((i,j,ni,nj))
            return dfs(ni,nj,area,size,grey, black,route)
        elif area[ni][nj] == area[i][j] and (ni,nj) in grey and not (ni,nj, i,j) in route:
            grey.append((i,j))
            print(f'GREY {i,j,ni,nj}\n')
            return come_back(area,grey,ni,nj)

    else:
        if grey:
            last_grey = grey.pop()
        else:
            black.append((i,j))
            print(f'BLACK {i,j}\n')
            return False
        black.append((i,j))
        print(f'black {i,j} last black\n')
        return dfs(last_grey[0],last_grey[1],area,size,grey,black,route)


def check_win(area,player):
    for i,row in enumerate(area):
        for j,v in enumerate(row):
            if v != '+':
                dfs_check = dfs(i,j,area,size)
                if dfs_check:
                    return draw_area(dfs_check)
                else:
                    continue
    return area
'''














def come_back(area,grey,i,j):
    '''
    comes back through grey points
    '''
    for k,n in enumerate(grey): 
        if n == (i,j):
            grey = grey[k:]
    # print(grey)

    for i in grey:
        area[i[0]][i[1]] = 'ob'
    return area

def dfs(i, j, area, size, grey=None, black=None, route=None):
    if grey == None: grey = []
    if black == None: black = []
    if route == None: route = []

    for row, col in [(-1,1),(1,1),(0,1),(1,0),(1,-1),(-1,-1),(0,-1),(-1,0)]:
        ni,nj = i+row, j+col

        # if ni or nj are out of range
        if not ni >= 0 or not nj >= 0 or \
          ni > size or nj > size:
            continue

        if area[ni][nj] == area[i][j] and not (ni,nj) in grey and not (ni,nj) in black:
            grey.append((i,j))
            route.append((i,j,ni,nj))
            return dfs(ni,nj,area,size,grey, black,route)
        elif area[ni][nj] == area[i][j] and (ni,nj) in grey and not (ni,nj, i,j) in route:
            grey.append((i,j))
            return come_back(area,grey,ni,nj)

    else:
        if grey:
            last_grey = grey.pop()
        else:
            black.append((i,j))
            return False
        black.append((i,j))
        return dfs(last_grey[0],last_grey[1],area,size,grey,black,route)


def check_win(area,player):
    for i,row in enumerate(area):
        for j,v in enumerate(row):
            if v != '+':
                dfs_check = dfs(i,j,area,size)
                if dfs_check:
                    return dfs_check
    return area

