# Kruskal
"""
    Minimum spanning trees are used in water networks, electrical grids, computer networks

    Implementation:
    - Iterate over vertices ordered by cost ASC
        - Merge sort is employed
    - Cycle detection
        - Disjoint set is employed to keep account of vertices merged by the algorithm
"""

def merge_sort(arr, key = None):
    if len(arr) <= 1:
        return arr
    
    if key is None:
        key = lambda x: x

    segment_size = 1

    arr2 = [None for _ in range(len(arr))]
    while segment_size < len(arr):
        for i in range(0, len(arr), segment_size * 2):
            first_slice = arr[i:i+ segment_size]
            second_slice = arr[i+segment_size:i + 2* segment_size]
            push_index = i
            while first_slice and second_slice:
                if key(first_slice[0]) <= key(second_slice[0]):
                    arr2[push_index] = first_slice.pop(0)
                else:
                    arr2[push_index] = second_slice.pop(0)
                push_index += 1
            rest = first_slice if first_slice else second_slice
            for r in rest:
                arr2[push_index] = r
                push_index += 1
        arr = arr2
        segment_size *= 2
    return arr


def test_merge_sort(): 
    arr = [ (10-i, i) for i in range(10)]
    s0 = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1), (10, 0)]
    s1 = [(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9)]
    assert s0 == merge_sort(arr=arr, key= lambda x: x[0])
    assert s1 == merge_sort(arr=arr, key= lambda x: x[1])

test_merge_sort()

# ------------------------------------

class DisjointSet:

    parent = {}


    def __init__(self, universe):
        self.make_set(universe)


    def make_set(self, universe):
        for i in universe:
            self.parent[i] = i

    
    def find(self, k):
        while self.parent[k] != k:
            k = self.parent[k]
        return k


    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        self.parent[pa] = pb



# -- Kruskal

from itertools import chain

def kruskal_minimum_spanning_tree(graph):

    mst = []

    universe = chain.from_iterable([ x[:2] for x in graph])
    disjoin_set = DisjointSet(universe)
    sorted_edges_graph = merge_sort(graph, key= lambda x: x[2])

    for u, v, cost in sorted_edges_graph:
        pu = disjoin_set.find(u)
        pv = disjoin_set.find(v)
        if pu != pv:
            disjoin_set.union(pu, pv)
            mst.append((u,v, cost))

    return mst


def test_kruskal():
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    answer = [(0, 3, 5), (2, 4, 5), (3, 5, 6), (0, 1, 7), (1, 4, 7), (4, 6, 9)]
    assert answer == kruskal_minimum_spanning_tree(edges)

test_kruskal()