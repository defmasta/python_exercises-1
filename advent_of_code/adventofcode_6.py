
""" Advent of Code exercise 6 """
""" Determine the number of trees you would encounter if, 
for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; 
multiplied together, these produce the answer 336."""

# description https://adventofcode.com/2020/day/3#part2

test = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""

string_map = """.#......#..####.....#..#.......
#.#...#...#..#.#...#.#...##.##.
#.#....#..........#...##.....##
#.#.#.....##......#.#.......###
..#..###....#.#....#.#.#..#....
.......#.#....##..##...#...#...
..#..#..#..###.......#.....#.#.
.#.......#...##...##.##......##
#.#.##..##.#..#....#..###..#.#.
#.....#.#.........#.....##.#.#.
..#.#....##..#...#...##........
......#....#..##.#.#......###..
.......#.......#......##...#...
.##.....#.......#...###.....##.
.#...#.##..##.#..##....#.......
..#......##...#..#...#.#.##.###
.##.##.....##....#..#......#.#.
.#.....#..###..#.##.#.....##.#.
......##..........#..........#.
.##....#.....#..##.#..#.#..###.
..##.......#....#...##...#..#..
.##...#.....#.###.#.#..#...#.#.
.....##.#.##..##...#...........
..#..###.##.#.#.###...###..#.#.
.#........#..#.#........#.#...#
....##.......#....#.#.##.#.....
....##........######..###..#.#.
#.#.#............#.......#..#..
...##...#.##.....#.#..#......#.
......#.##.#....##..#.#..###...
##.....#.#....#....#.##.#.###..
#..#..#..##.#..##.##.##.#.##...
.###.####..#..#........#.....##
.......##..#.......#...........
.##...#............#.#.##...#..
....##.....#...##..#..#.#..###.
...#.....#####.#..#...##....##.
#.....#.#.#....##.......##.#.#.
......#.#..#.##.#######......#.
#.##...##....#..###.#.......#..
.....##...#....#...#....##.##.#
....###......#...###..#......##
..#...##..##.######..#.#......#
......##....#....##..#......##.
.#...#..##..#.###.#......#....#
##....##..#..####.#.....#...#..
.#.......#...#.......##......#.
......#...#...#........#.......
.#........#.###...#..####.#..#.
##...#.#............#.....###..
.....###.#.##...........###..#.
.#.#...#.....#.#.##..##...####.
..##.......#..#.##.#....#.....#
.#..#.#..####.....###.#.....#..
..#..###.....####..#.##.#.#.##.
.###..#.....#......#...####....
...#.#..#.#..#...#...#....##.##
..###....#.##.....#..........#.
###...#####......##............
..###.....#........##.#...#..#.
..##.##.#.....##........##..#.#
##..#.#...#.#..#..###.#....#..#
....#..#.#.....#..#####...#....
....#.........#......##.##.....
.#...####.##......##..##.#..#.#
...#...#.##..#...##..###...#...
###...#.....#.##.###.###..#.#..
..#......#.###.....#..##.#...#.
#.....##.########...#####....#.
........##..#..##..##.#........
....#.######....##..#..#.##..#.
#.......#..##..#..#.#.#..##.##.
...#.#..#..#.......#......###.#
.#.#..#.#..#.##.#.............#
#....#.##.#.#.....#..#.#..#....
...###..#...#....#.........#.#.
.#..#.....##..#.#..#.#.......#.
..#...##...#......#......####..
....#..#.......#.......#.#..#..
#...#..#...........#.#..#.....#
#...#.#.......#...#....###....#
.#..#.#.##....#......#........#
..#...#..##..#..#..#..#...#.#..
..#.#.........#....#....##.....
##.....##.#.#.#.........##.....
.##...#.##...........#...#...##
.##..##.#.#..........##..##....
#....#....#.#...#.#..#....#.#..
####....##.....#..##.###.......
#..#....#......##.#.#....#.....
.....#....#.###.##.........###.
#.......#.####..#..#..##.......
##.#.......#..##..#....#..#.#..
..###...#.#...#.....##.##.####.
....#...#.#....#..#..#.....#.##
#.....##.#.#..#.##..#..##......
................###..#....##...
..#.##.....#..........##.#...#.
..#.#..#.#....#.#.#..#..#..#.#.
#...#..##.#.#...#..#...#..#....
#..#.#.........#..###........#.
.#...#.............#..###..#..#
#.........#.#..#...#.#.....#..#
....#..#..#.#.#...#...#.....##.
##...###.#.####..#......#...#..
..#..##...#.#......#.#.......#.
#......###....##.#.##..........
#####....###..#...............#
##.#...####....#....#...#....#.
.#.......#..#.....#...#.....###
...#..#.#.#....##......##...#..
...#.....#...#.##.#..#.#....#..
#...###....#...#.#....#........
.#.......#........#...##.##.##.
.....#....#...##.....##...###.#
....#....#.#..#...##.##.##.....
.......#............#...#.#..#.
.#............#.....##.......#.
........#....#....##......##.##
.......##..#.#..#.##..###..##.#
#..##..##.........####.#.###...
#....#..#...##...#.............
#...#...###..........##..#..#..
....#...#..#.....##...#........
#.....#......#.#.....#...#..#..
..#.....#.....#....#..#........
..#..#.....#.#.........#..###..
................###..#.#....#..
#.....#.....#.#.#.#.#..#...#.#.
#....#....#.#..........#.#....#
....#..#......#..##.#...##.....
..#.#...#.####....#.#..#.#..#..
.........##......#.....##......
##.#.###.#.....#.....####.#..#.
.....#.....#..#....#..###.#....
##..#.#...#.##....#....#.......
.....#......#.#...##..#.#......
....##..#...#...##..##.#....#.#
............#..........##.#....
##..#..#.##..##..#.#....#.#.#..
.......#.#...#...#.#...#..#....
#....#.#...#...#........#..#...
...........#.......#...##..###.
.#..##......#.##.........##..#.
...#...#...###.#.##....##.#..#.
#...#..#.#.#.....##..#.......#.
.##..#.###.##......#.#....#.#.#
..#....#.......#..#..#.#.#.##..
#...#...###...###.........#....
.#.#...#.....##.#.#..#....#.##.
.........#.#.##.....#.#.###....
...#.#...#......#...####......#
...##..##....##......##...###..
###...#..#.......##.....#....#.
...#..#..#..###...##.##..#..#..
...#......#......##..#.#.##..#.
...#.........#....#.#....#.#...
##................#..#.#.....#.
....#.##...#..#.##...##.#.....#
......#..##.##..###.#..#.##.##.
.#.#...###.....###.....##...###
.##.....#.#.#..#..###..#..#..#.
#.......#..#..#....##.....#....
...#.#.##..#..#......##.##...#.
....##.#......#...#..#..#......
.####.#..#.....#..##.#...##..##
..#..#...#..........###..#....#
.#.#.##.##...#............#....
........##..##......#.##..#.###
...#.#....###......##.......#..
..##...#...#.#..#.....#.....#..
##..#...###..#..#.#.#...#...#..
.....#..#....##.....##.....###.
....##...###.#..#.#....##..#..#
#......#...#....#......#...##..
....#.##...#.#......#.#.##...#.
.......#.....#...#####...#.#...
...#.....##.#............#.....
...#.#........#.#.#..#.........
....###......#.#.#..#.####.#..#
#.....#.#.#.....#.#.#.....#..#.
..##.##......#...#.#...........
###..###....#.#####......###...
..##..............##.#.#....#.#
#..#...#..........#..#.#.#..###
##.###............#....#.#...#.
#.#..#.#..##.#.#....#...#......
#....#...#..##.....#..#.#..###.
..#.....#.#....#.#..#.##.#..##.
...##...#.#.##...#....###....#.
......###.####.......#..#.#.#.#
.#..............##........#....
...##.##...##....#..#.......#..
.....#.....#....###...#..#..#.#
.#.....#..#.....#......#.....##
#.#.##.#..#..#.....#.##..###...
..#......#...##.###..#.#...#..#
......#.....#...##......#......
##.#........#..........#.....#.
#........##.#............##....
...#......##...#.#.....##......
...##.......#....#.#..#.#.###..
..#....##..##.##.....###....#..
..#...#.#...#.....#..........#.
......#...#...#.#.##.#...#.#.#.
.#...#......#.##........#......
.##.##..#....#...#.#...##......
#..#......#.#...........#....#.
....##.#....#...#..#....#.#..##
#....##.##....#.#..##.#........
.##.##.#....##.....#..#....#..#
...#...#.....###.#.##..........
....#...#....##.......###......
#.........#......#.#.......#...
#..........#..##..#.#..........
.....#.......#..##.##....##...#
........................#.#....
#..#.........#.............#..#
#..#.....#.......#....#....#.#.
..##..##.......##....#...#.....
.##......#..##......#.###......
...#.#........#.......##..###..
..##...###.###......#...#....##
#...#...#.....###.#.#.#..#.....
#....#.........#..##...#...##..
#..###..#.#.#.##.#..#.#....#.##
#...#.#.....#.###.#.......#....
..##..#..#....#.#...........#.#
#.........#.#......#...##......
.######......#..#....#.#.#....#
##..#.#..####.###.........#....
###########.....##.##...#..#...
#...##.#.#....#.#....#......#..
...#..##..#..##..#......#....#.
.#....#...#....#.#..##....##...
#..#.#............#....#.#...#.
...#...#..#.#.##......#..#.#...
#.#...##.....#..#.##......####.
.#.#..##..#.....#.#..#.##......
#.#.##......##.....#..#.#..#...
#..##...#.##.#.......#.##......
..#.......#.#.#...##..##...#...
.#...#..#..#.#.........#..##...
#..#.......#....#.#...#.###...#
.......#..#.......##.#.#...#.#.
.#.................###.#..###..
..........#.#.....##..#####...#
#......#.#..##.#.#...#.##.#....
#......#.#..##.##.#...#....#...
....#..#......#....#....#######
.#...#......#....###......#.###
#.#....#.#...#.###......#..#..#
.###......#.#...#.####.#..####.
######.#.....###.#...#.#.....#.
.#.###....#..#.#.....#.....####
.......###.#.........#..#......
#...#.....##.#......####.......
..#.#..##.#.#...#...#..##..##..
.....#...##.....#...##......##.
##..#..#.##..#.#......#.....#..
##.........#.#.##.#..#.#....#.#
.#........###...#.........#....
...#..#.#..#....####...........
#.#....#..##..####.#...#.##....
.#.....#.......#..........#..##
...#.......#...###..#.....#..##
.........#.###.#..##...#.##...#
.#..........##..####...#..#.#.#
.#...##...#............##...#.#
...#....#.#..........#.#..#.#..
.#.#...##....##.#.#.#....#.....
....#..#.....#.#..#.#..#.##.###
.....#.#.....#..#......#.#.#...
.....#.#.#..###..#.#..###...#..
#.......####...#.#..#......##.#
....#..#..###......###.##....#.
##.....#.....#.............#..#
#..#..#...##.....##..#..#.#....
.....#.#.###...#...............
#.#.#.....#.#..#.#...#.......#.
..##.##............#....#..##..
#....##...#.....#.###...#.#....
#...##.#.........#...#....#....
##.##.#...#.#...###..#....##..#
....#....##..#..#.......#...##.
.#...#...#..#.....#..###.#..#.#
....#..###......#....##....#...
#.#.....#....##.#..#.#...###...
.......#............#......#...
.##..#.###.#.............###...
..##...##.#.#.#.....#........##
....#.###....#..#..#...#...#..#
.....#...#...#..#....#.....##..
###.#.#.....#......####.....#..
#.#.###............#......#....
..#.....#..#..#..#....#......#.
#...######...#....#.##...##.#.#
##.#.#.#..##......##.#..#.#...#
............#.#..#.##....#.....
......#............#.#...#..#.#
.#..##...##..#.#.#..###.....##.
#.###.#...........#...#....#...
....##.....#...##...#...###.#.#
.####.#.#.....#.#..#.#.##......
.#...##......###...#..##..#.#..
.#......#...#....##.....##..#..
..........##.....###.##.#...#.#
.#........##.#..............#..
#...###..#...#.....#....#.....#
...#......#..#...#...#..###.#..
.#...##..#........#.......#.#..
.#.#.##.........##.##......#..#
#...#.#.#...#.....#.#...#.#..#.
#.#..#...#...#...##..........#.
.#...........#....#..#.#..#.#..
#.......#......#..#...#........
.....#..#...##..###..##........
......#...#.....#..#.#.#....##.
....##..##..##....###.##.......
.#........##.#.#...#..#........
.....##...##...#......#..#...#.
..#.....#....###.#..##....#..#.
......#..#...####.#.....##.####
"""


def read_in_map(data, num):

    # split string at every new line
    map_split = data.split('\n')

    # delete empty elements in the list
    clean_map = [x for x in map_split if x]

    # create map with repeated slopes
    rep = len(clean_map[0]) // num
    rep = (len(clean_map) // rep) + 1 # just to make sure there is enough reps
    full_map = []
    for i in clean_map:
        rep_slice = i * (rep)
        full_map.append(rep_slice)
    print(rep)
    return full_map


def check_slope(data, r, d):

    map = data
    right = r
    down = d
    tree = 0
    n = 0

    while n < len(map):
        if n > 0:
            if map[n][right] == '#':
                tree += 1
            else:
                pass
            right += r
        n += down
    print("Right {}, down {}, there are {} trees.".format(right, down, tree))
    return tree


# right and down combinations
combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1
for i in combinations:
    right = i[0]
    down = i[1]
    result = check_slope(read_in_map(string_map, right), right, down)
    product *= result
print("Product: ", product)

#read_in_map(string_map,1)
#check_slope(read_in_map(string_map, 1), 1, 1)

