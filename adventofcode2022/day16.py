import re
import heapq
from typing import List, Dict
from itertools import permutations
from collections import namedtuple


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.distances = {}
        self.name = name
        self.connections = connections
        self.flow_rate = flow_rate
        self.visited = set()


def load_valves(path):
    valves = {}

    for line in open(path).read().splitlines():
        matches = re.match(r'Valve ([A-Z]+) has flow rate=(\d+); .* valves? ([A-Z ,]+)$', line)
        groups = matches.groups()

        name = groups[0]
        flow_rate = int(groups[1])
        connections = groups[2].split(', ')
        valves[name] = Valve(name=name, flow_rate=flow_rate, connections=connections)

    return valves


def explore_from_valve(valve, valves: Dict[str, Valve]):
    queue = [(valve, 0)]
    visited = set()

    while queue:
        current_name, dist = queue.pop(0)
        current = valves[current_name]

        if current_name != valve and current.flow_rate > 0:
            valves[valve].distances[current_name] = dist

        visited.add(current_name)

        for connection in current.connections:
            if connection in visited:
                continue

            queue.append((connection, dist+1))


def dfs(valve, valves: Dict[str, Valve], time: int, opened_at: Dict[str, int]):
    current = valves[valve]

    if current.flow_rate > 0:
        time += 1
        opened_at[valve] = time

    current_score = 0

    for opened_name, time_opened in opened_at.items():
        current_score += valves[opened_name].flow_rate * (30 - time_opened)

    best_score = current_score

    for next_valve_name, next_valve_distance in current.distances.items():
        if next_valve_name in opened_at:
            continue

        if time + next_valve_distance >= 30:
            continue

        next_score = dfs(next_valve_name, valves, time + next_valve_distance, opened_at=dict(opened_at))
        best_score = max(next_score, best_score)

    return best_score


def explore_graph_dual(valves: Dict[str, Valve]):
    State = namedtuple('Point', ['prio', 'valve_us', 'valve_us_time', 'valve_us_path', 'valve_ele', 'valve_ele_time', 'valve_ele_path', 'opened_at'])
    queue: List[State] = [State(prio=1, valve_us='AA', valve_us_time=1, valve_ele='AA', valve_us_path='', valve_ele_time=1, valve_ele_path='', opened_at={})]
    live_elements = set(valves['AA'].distances.keys())
    possible_solutions = []

    while queue:
        state = heapq.heappop(queue)

        if state.valve_us_time == state.valve_ele_time:
            for next_us, next_ele in permutations(set(live_elements) - set(state.opened_at.keys()), r=2):
                next_us_time = valves[state.valve_us].distances[next_us] + state.valve_us_time + 1
                next_ele_time = valves[state.valve_ele].distances[next_ele] + state.valve_ele_time + 1

                prio = min(next_us_time, next_ele_time)

                if prio >= 26:
                    continue

                new_opened_at = dict(state.opened_at)

                if next_us_time < 26:
                    new_opened_at[next_us] = next_us_time
                else:
                    next_us = state.valve_us
                    next_us_time = state.valve_us_time

                if next_ele_time < 26:
                    new_opened_at[next_ele] = next_ele_time
                else:
                    next_ele = state.valve_ele
                    next_ele_time = state.valve_ele_time

                possible_solutions.append((new_opened_at, state.valve_us_path + '-' + next_us, state.valve_ele_path + '-' + next_ele))

                heapq.heappush(queue, State(prio=prio,
                                            valve_us=next_us,
                                            valve_us_time=next_us_time,
                                            valve_us_path=state.valve_us_path + '-' + next_us,
                                            valve_ele=next_ele,
                                            valve_ele_time=next_ele_time,
                                            valve_ele_path=state.valve_ele_path + '-' + next_ele,
                                            opened_at=new_opened_at,
                                            ))

        elif state.valve_us_time < state.valve_ele_time:
            for next_us in set(live_elements) - set(state.opened_at.keys()):
                next_us_time = valves[state.valve_us].distances[next_us] + state.valve_us_time + 1

                if next_us_time >= 26:
                    continue

                prio = min(next_us_time, state.valve_ele_time)
                new_opened_at = dict(state.opened_at)
                new_opened_at[next_us] = next_us_time
                possible_solutions.append((new_opened_at, state.valve_us_path + '-' + next_us, state.valve_ele_path))

                heapq.heappush(queue, State(prio=prio,
                                            valve_us=next_us,
                                            valve_us_time=next_us_time,
                                            valve_us_path=state.valve_us_path + '-' + next_us,
                                            valve_ele=state.valve_ele,
                                            valve_ele_time=state.valve_ele_time,
                                            valve_ele_path=state.valve_ele_path,
                                            opened_at=new_opened_at,
                                            ))

        elif state.valve_ele_time < state.valve_us_time:
            for next_ele in set(live_elements) - set(state.opened_at.keys()):
                next_ele_time = valves[state.valve_ele].distances[next_ele] + state.valve_ele_time + 1

                if next_ele_time >= 26:
                    continue

                prio = min(next_ele_time, state.valve_us_time)
                new_opened_at = dict(state.opened_at)
                new_opened_at[next_ele] = next_ele_time
                possible_solutions.append((new_opened_at, state.valve_us_path, state.valve_ele_path + '-' + next_ele))

                heapq.heappush(queue, State(prio=prio,
                                            valve_us=state.valve_us,
                                            valve_us_time=state.valve_us_time,
                                            valve_us_path=state.valve_us_path,
                                            valve_ele=next_ele,
                                            valve_ele_time=next_ele_time,
                                            valve_ele_path=state.valve_ele_path + '-' + next_ele,
                                            opened_at=new_opened_at,
                                            ))

    converted_scores = []

    for opened_at in possible_solutions:
        converted_scores.append((opened_at_score(opened_at[0], valves), opened_at[1], opened_at[2], opened_at))

    for score in converted_scores:
        if score[1].startswith('-JJ-BB-CC') and score[2].startswith('-DD-HH-EE'):
            pass

    result = sorted(converted_scores, reverse=True)
    return result[0][0]


# us: JJ (4), BB (8), CC (10)
# ele: DD (3), HH (8), EE (12)


def opened_at_score(opened_at, valves):
    current_score = 0

    for opened_name, time_opened in opened_at.items():
        current_score += valves[opened_name].flow_rate * (27 - time_opened)

    return current_score


def max_pressure_release(path):
    valves = load_valves(path)

    for name, valve in valves.items():
        explore_from_valve(name, valves)

    return dfs('AA', valves, time=0, opened_at={})


def max_pressure_release_dual(path):
    valves = load_valves(path)

    for name, valve in valves.items():
        explore_from_valve(name, valves)

    return explore_graph_dual(valves)


def test_max_pressure_release():
    assert max_pressure_release('input/16.test') == 1651


def test_max_pressure_release_dual():
    assert max_pressure_release_dual('input/16.test') == 1707


if __name__ == '__main__':
    print(max_pressure_release('input/16'))
    print(max_pressure_release_dual('input/16'))
