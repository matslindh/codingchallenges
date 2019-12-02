import re
from operator import itemgetter, attrgetter, methodcaller


def calc_dmg(attacker, defender):
    dmg_modifier = 1

    if attacker['damage_type'] in defender['immune']:
        dmg_modifier = 0
    elif attacker['damage_type'] in defender['weak']:
        dmg_modifier = 2

    return attacker['damage'] * attacker['units'] * dmg_modifier


def battle(f):
    groups = []

    armies = {
        'immune': [],
        'infection': [],
    }
    active_type = 'immune'

    for line in f.readlines():
        line = line.strip()

        if not line:
            active_type = 'infection'

            continue
        elif line.endswith(':'):
            continue

        matches = re.match(r'([0-9]+) units each with ([0-9]+) hit points (\(.*\))? ?with an attack that does ([0-9]+) ([a-z]+) damage at initiative ([0-9])', line)
        m_groups = matches.groups()

        weak = []
        immune = []

        if m_groups[2]:
            for l in m_groups[2][1:-1].split(';'):
                parts = l.strip().split(' to ')
                types = [p.strip(',').strip() for p in parts[1].split(',')]

                if parts[0] == 'weak':
                    weak = types
                else:
                    immune = types

        g = {
            'units': int(m_groups[0]),
            'hp': int(m_groups[1]),
            'weak': weak,
            'immune': immune,
            'damage': int(m_groups[3]),
            'damage_type': m_groups[4],
            'initiative': int(m_groups[5]),
            'type': active_type,
            'group_no': len(armies[active_type]) + 1,
            'attacking': None,
        }

        groups.append(g)
        armies[active_type].append(g)

    while armies['immune'] and armies['infection']:
        selection_order = sorted(groups, key=lambda g: (g['units'] * g['damage'], g['initiative']), reverse=True)
        selected = {
            'infection': {},
            'immune': {},
        }

        for group in selection_order:
            target = 'infection' if group['type'] == 'immune' else 'immune'
            best = None

            for idx, defender in enumerate(armies[target]):
                if idx in selected[target]:
                    continue

                dmg = calc_dmg(group, defender)

                if dmg == 0:
                    print(group['type'].capitalize() + ' group ' + str(group['group_no']) + ' would not deal damage to ' + defender['type'].capitalize() + ' group ' + str(defender['group_no']))
                    continue

                sorter = (dmg, defender['units'] * defender['damage'], defender['initiative'], idx)
                print(group['type'].capitalize() + ' group ' + str(group['group_no']) + ' would deal defending group ' + str(defender['group_no']) + ' ' + str(dmg) + ' damage')

                if best and best[0] == sorter[0] and best[1] == sorter[1]:
                    print("+beep", best, sorter)

                if not best:
                    best = sorter
                elif sorter > best:
                    print("prev", best)
                    print("+new", sorter)
                    best = sorter

            if best:
                defender = armies[target][best[3]]
                print(group['type'].capitalize() + ' group ' + str(group['group_no']) + ' attacks ' + str(defender['type'].capitalize()) + ' ' + str(defender['group_no']))
                group['attacking'] = (best[3], best[0])
                selected[target][best[3]] = True

        print('Immune')
        for group in armies['immune']:
            print('Group ' + str(group['group_no']) + ' contains ' + str(group['units']) + ' units')

        print('Infection')
        for group in armies['infection']:
            print('Group ' + str(group['group_no']) + ' contains ' + str(group['units']) + ' units')

        print('')

        for group in sorted(groups, key=lambda g: g['initiative'], reverse=True):
            print(group['type'], group['attacking'])
            if group['attacking'] is None:
                print(group['type'].capitalize() + ' group ' + str(group['group_no']) + ' does not attack ')
                continue

            target = 'infection' if group['type'] == 'immune' else 'immune'
            defender = armies[target][group['attacking'][0]]

            if group['units'] <= 0 or defender['units'] <= 0:
                continue

            units_lost = calc_dmg(group, defender) // defender['hp']
            #print(calc_dmg(group, defender) / defender['hp'])
            #print('dmg', group['attacking'][1], 'def_units', defender['units'], 'def_hp', defender['hp'], 'lost', units_lost)
            print(group['type'].capitalize() + ' group ' + str(group['group_no']) + ' attacks defending group ' + str(defender['group_no']) + ', killing ' + str(min(units_lost, defender['units'])) + ' units with ' + str(calc_dmg(group, defender)) + ' damage')
            defender['units'] -= units_lost

        groups = list(filter(lambda g: g['units'] > 0, groups))

        for g in groups:
            g['attacking'] = None

        for k in armies:
            armies[k] = list(filter(lambda g: g['units'] > 0, armies[k]))

        print('-----')

    print(groups)
    return sum([group['units'] for group in groups])


def test_battle():
    assert battle(open('input/24.test')) == 5216

# 17500 - too low
# 18352 - too high
if __name__ == '__main__':
    print(battle(open('input/24')))
