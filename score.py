# -*- coding: utf-8 -*-

import bowling as b
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--result', dest='game_result', help='Game data')
args = parser.parse_args()
try:
    res = b.get_score(args.game_result)
except ValueError as exp:
    print(exp)
else:
    print(f'In game {args.game_result} scores {res}')

