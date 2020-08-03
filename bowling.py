def get_score(game_res):
    correct_input = '123456789/X-'
    score = 0
    list_result = []
    frame = []
    for ch in game_res:
        if ch not in correct_input:
            raise ValueError('Inappropriate value!')
        elif ch == 'X':
            list_result.append(ch)
            if len(frame) == 1:
                raise ValueError('One throw before Х')
        else:
            frame.append(ch)
            if len(frame) == 2:
                list_result.append(frame)
                frame = []
    if len(frame) == 1:
        raise ValueError('Superfluous meaning!')
    if len(list_result) != 10:
        raise ValueError('Not 10 frames played!')
    for i in list_result:
        if i == 'X':
            score += 20
        elif i[1] == '/':
            score += 15
        elif i[0] == '/':
            raise ValueError('Spare can\'t be on the first strike!')
        elif i[0] == i[1] == '-':
            continue
        elif i[0] == '-':
            score += int(i[1])
        elif i[1] == '-':
            score += int(i[0])
        else:
            if int(i[0]) + int(i[1]) > 10:
                raise ValueError('Amount more 10')
            for k in i:
                if k != '-':
                    score += int(k)
    return score

if __name__ == '__main__':
    game_result = '53--X441/-622X918/'
    try:
        res = get_score(game_result)
    except ValueError as exp:
        print(exp)
    else:
        print(f'In game {game_result} scores {res}')