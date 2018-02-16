import itertools
import re
import sys
import time
import yaml

def spinner(duration=10):
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    for _ in range(duration*5):
        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\b')


def dictionary_dump(filename, **kwargs):
    with open(filename, 'w') as file:
        yaml.dump(kwargs, file, default_flow_style=False)


def bowling_score(game):

    '''
    >>> bowling_score('XXXXXXXXXXXX')
    300
    '''
    total = 0
    spare = False
    strike_1 = False
    strike_2 = False

    for roll in game:
        if int(roll) in range(10):
            total += int(roll)
        if roll == '-':
            total += 0
        if roll == '/':
            pass

    return total
