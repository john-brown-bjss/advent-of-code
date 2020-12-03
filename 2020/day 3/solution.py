import os
import re
from math import ceil, prod


class GridTraverser():

    def __init__(self, debug=False, x_increment=3, y_increment=1):
        self.x_increment = x_increment
        self.y_increment = y_increment
        self.grid_template = self.extrapolate_grid(debug)
        self.height = len(self.grid_template)
        self.tree_marker = '#'

    def extrapolate_grid(self, debug):
        if debug:
            return [
                '..##.........##.........##.........##.........##.........##.......',
                '#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
                '.#....#...#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
                '..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
                '.#...##..#..#....##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
                '..#.##.......#.#.#.......#.##.......#.##.......#.##.......#.##.....',
                '.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
                '.#........#.#........#..#........#.#........#.#........#.#........#',
                '#.##...#...#.##...#...#.#.#...#...#.##...#...#.##...#...#.##...#...',
                '#...##....##...##....##...##.....##...##....##...##....##...##....#',
                '.#..#...#.#.#..#...#.#.#..#...#..#.#..#...#.#.#..#...#.#.#..#...#.#'
            ]
        else:
            path = os.path.join(os.path.dirname(__file__), 'inputs.txt')
            with open(path, 'r') as file_handle:
                grid = []
                template = file_handle.read().splitlines()

                grid_height = len(template)
                required_width = (ceil(grid_height / len(template[0]))) * self.x_increment
                for row in template:
                    grid.append(row * required_width)
                return grid

    def get_point_in_traverse(self, x, y):
        grid = self.grid_template[y]
        points = grid[x:x+self.x_increment + 1]
        return points[-1]

    def contains_tree(self, point):
        return int(point == self.tree_marker)

    def get_number_of_trees(self):
        total_trees = 0
        x = 0
        y = 1
        while(y < self.height):
            point = self.get_point_in_traverse(x, y)
            total_trees += self.contains_tree(point)
            x += self.x_increment
            y += self.y_increment
        return total_trees


def calculate_slopes(slopes):
    total_trees = []
    for x_increment, y_increment in slopes:
        traverser = GridTraverser(debug=False, x_increment=x_increment, y_increment=y_increment)
        trees = traverser.get_number_of_trees()
        total_trees.append(trees)
    return total_trees

if __name__ == "__main__":
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    trees_in_slopes = calculate_slopes(slopes)
    print(f'Trees for solution a: {trees_in_slopes[1]}')
    print(f'Trees for solution b: {prod(trees_in_slopes)}')