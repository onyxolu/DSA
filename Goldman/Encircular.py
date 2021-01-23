def isRobotBounded(commands):
    
    direction = 'N'
    startDir = 'N'
    
    dirs = {
        'N': {
            'L': 'W',
            'R': 'E'
        },
        'W': {
            'L': 'S',
            'R': 'N'
        },
        'S': {
            'L': 'E',
            'R': 'W'
        },
        'E': {
            'L': 'N',
            'R': 'S'
        },
    }
    
    pos = {
        'V': 0,
        'H': 0
    }
    for ins in commands:
        if ins == 'G':
            if direction == 'N':
                pos['V'] += 1
            elif direction == 'S':
                pos['V'] -= 1
            elif direction == 'W':
                pos['H'] -= 1
            elif direction == 'E':
                pos['H'] += 1
        else:
            direction = dirs[direction][ins]
            
    if direction == startDir and pos['V'] + pos['H'] != 0:
        return False
    
    return True