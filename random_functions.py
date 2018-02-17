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
    >>> rf.bowling_score("-9,18,27,36,45,45,36,27,18,-9")
    90
    >>> rf.bowling_score("09,18,29,36,45,45,36,27,18,09")
    ERROR: How did you knock down more than 9 pins and not get a spare or strike?
    False
    >>> bowling_score('X,X,X,X,X,X,X,X,X,X,X,X')
    300
    '''
    total = 0

    frames = game.split(',')
    for i, frame in enumerate(frames):
        if len(frame) > 2:
            print "ERROR: Too many rolls in this frame"
            return False
        if frame == 'X':
            # look ahead 2 rolls
            pass
        elif frame.endswith('/'):
            # look ahead 1 roll
            pass
        else:
            total_this_frame = 0
            for roll in frame:
                if roll == '-':
                    roll = 0
                total_this_frame += int(roll)
            if total_this_frame <= 9:
                total += total_this_frame
            else:
                print ("ERROR: How did you knock down more than 9 pins and " +
                      "not get a spare or strike?")
                return False

    return total
