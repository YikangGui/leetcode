# Jack Builds Road to Connect Cities and Towns

'''
def solve(grid):
    cities = {...} # location of cities

    def bfs(source):
        return {place : distance from source to that (non-hill) place}

    distopt = collections.defaultdict(lambda: float('inf'))
    distmap = collections.defauldtict(dict)
    mstedges = []
    #distmap[city][place] = distance from city to that place
    for city in cities:
        distmap[city] = dist = bfs(city)
        for place, d in dist.items():
            distopt[place] = min(distopt[place], d)
            if place in cities and city < place:
                mstedges.append((d, city, place))

    ans = sum(distopt.values())
    # now add mst edges
    mstedges.sort()
    dsu = DSU()

    for d, u, v in mstedges:
        if dsu.union(u, v):
            ans += (d // 2) * (d + 1) // 2

    return ans
'''
from collections import defaultdict
import copy

grid = ['$..#', '..#.', '#.$.', '$...']
grid = ['$...','....','....','..$.']


def solution(grid):
    m = len(grid)
    n = len(grid[0])
    cities = set()
    map = []
    unvisited = []
    for i, row in enumerate(grid):
        tmp = []
        tmp_unvisited = []
        for j, loc in enumerate(list(row)):
            if loc == '$':
                cities.add((i, j))
            if loc != '#':
                tmp_unvisited.append(True)
            else:
                tmp_unvisited.append(False)
            tmp.append(loc)
        map.append(tmp)
        unvisited.append(tmp_unvisited)
    # print(map)
    # print(cities)

    def bfs(i, j, unvisited):
        q = [(i, j, 0)]
        while q:
            tmp = q.pop(0)
            if 0 <= tmp[0] < m and 0 <= tmp[1] < n and unvisited[tmp[0]][tmp[1]]:
                unvisited[tmp[0]][tmp[1]] = False
                distmap[(tmp[0], tmp[1])] = tmp[2]
                for x, y in (0,1),(0,-1),(-1,0),(1,0):
                    q.append((tmp[0]+x, tmp[1]+y, tmp[2]+1))

    distopt = defaultdict(lambda: float('inf'))
    distmap = dict()
    mst_edges = []

    for city_x, city_y in cities:
        cur_unvisited = copy.deepcopy(unvisited)
        bfs(city_x, city_y, cur_unvisited)
        # print(distmap)
        for (i, j), dist in distmap.items():
            if (i, j) not in cities:
                distopt[(i, j)] = min(distopt[(i, j)], distmap[(i, j)])
            if (i, j) in cities and (i, j) > (city_x, city_y):
                mst_edges.append((dist, (city_x, city_y), (i, j)))
    res = sum(distopt.values())
    # print(cities)
    # print(res)
    # print(distopt)

    mst_edges.sort()
    # print(mst_edges)

    cities_state = dict()
    for city in cities:
        cities_state[city] = -1

    def find(city):
        while isinstance(cities_state[city], tuple):
            city = cities_state[city]
        return city

    def union(city1, city2):
        city1_p = find(city1)
        city2_p = find(city2)
        city1_p_rank = cities_state[city1_p]
        city2_p_rank = cities_state[city2_p]
        if city1_p == city2_p:
            return False
        if city1_p_rank < city2_p_rank:
            cities_state[city2_p] = city1_p
            cities_state[city1_p] += city2_p_rank
        else:
            cities_state[city1_p] = city2_p
            cities_state[city2_p] += city1_p_rank
        return True
    for dist, city1, city2 in mst_edges:
        if union(city1, city2):
            res += ((dist-1) // 2) * ((dist) // 2) + dist

    print(res)


solution(grid)