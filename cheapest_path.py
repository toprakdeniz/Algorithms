# OUTPUT: find cheapest path

# APPROACH: 
# eleminate costly paths. 
# there is a cheapest cost map
# push move if it is the most effient move 
# pull move, push derivations only if it is still the most effient move
# all the moves should hold link to the path they take
# also holds the move that passenger performed to arrive t

moves = {
    "right": (0,1), 
    "left" : (0,-1),
    "up"   : (-1,0),
    "down" : (1,0)
}

def cheapest_path_bfs(t, start, finish):
       # maps are dims y x 
    cost_map = [[float("infinity") for j in range(len(t[0]))] for _ in range(len(t))]
    moves_map = [[ "" for j in range(len(t[0]))] for _ in range(len(t))]
    cost_map[start[0]][start[1]] = 0 # do not visit start
    moves_stack = [(start, 0)]
    
    while moves_stack:
        coord, cost = moves_stack.pop(0) # bfs
        if coord == finish: continue
        if cost > cost_map[coord[0]][coord[1]]:continue
        for m_name, move in moves.items():
            y = coord[0] + move[0]
            x = coord[1] + move[1]
            if x == -1 or y == -1 or y == len(t) or x == len(t[0]): continue
            path_cost = t[y][x] + cost
            if path_cost < cost_map[y][x]:
                moves_stack.append(((y,x), path_cost))
                cost_map[y][x] = path_cost
                moves_map[y][x] = m_name
            
    # reverse the moves
    coord = finish
    reverse_result = []
    while coord != start:
        move = moves_map[coord[0]][coord[1]]
        reverse_result.append(move)
        opposite = moves[move]
        coord = (coord[0] - opposite[0], coord[1] - opposite[1])
    return list(reversed(reverse_result))


# SOLUTION WITH HEAP

from heapq import heappush, heappop
import numpy as np

def cheapest_path_heap(t, start, finish):
    
    # heap sort always explores the cheapest paths first
    # so boolean map is enuogh to keep track of visited nodes
    visited_map = np.zeros((len(t), len(t[0])), dtype=bool)
    visited_map[start[0]][start[1]] = True
    queue = [(0, start, [])]
    
    while queue:
        value, coord, path = heappop(queue)
        if coord == finish: return path
        for m_name, move in moves.items():
            y = coord[0] + move[0]
            x = coord[1] + move[1]
            if x == -1 or y == -1 or y == len(t) or x == len(t[0]): continue
            path_cost = t[y][x] + value
            if visited_map[y][x] == False:
                heappush(queue, (path_cost, (y,x), path + [m_name]))
                visited_map[y][x] = True
    return []

import time

def test_cheapest_path():
    t = [
        [1, 1, 1, 1, 5],
        [1, 2, 3, 4, 1],
        [1, 2, 3, 4, 1]
    ]
    start = (0,0)
    finish = (2,4)
    start_time = time.time()
    assert cheapest_path_heap(t, start, finish) == ["right", "right", "right", "down", "right", "down"]
    for i in range(1000):
        cheapest_path_heap(t, start, finish)
    mid_time = time.time()
    assert cheapest_path_bfs(t, start, finish) == ["right", "right", "right", "down", "right", "down"]
    for i in range(1000):
        cheapest_path_bfs(t, start, finish)
    end_time = time.time()
    print("heap took: ", mid_time - start_time)
    print("bfs took: ", end_time - mid_time)
    print("all tests passed")


test_cheapest_path()
# heap took:  0.072998046875
# bfs took:  0.04799962043762207
# all tests passed