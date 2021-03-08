# Import required libraries

import re
from day2_c import get_total_wrapping_c, get_total_ribbon_c


# Read in input

with open('input', 'r') as f:
    z = f.read()


# Define pure Python functions for solving parts 1 & 2

def get_total_wrapping(z):

    total_area = 0
    pkg_regex = r"(\d+)x(\d+)x(\d+)"

    for pkg in re.findall(pkg_regex, z):

        # Get package dimensions as integers
        l = int(pkg[0])
        w = int(pkg[1])
        h = int(pkg[2])

        # Find smallest two sides (a & b)
        if h < w:
            a = h
            b = l if l < w else w
        else:
            a = w
            b = l if l < h else h

        # Calculate area + slack for present and add to total
        total_area += (2*l*w + 2*w*h + 2*h*l) + a*b

    return total_area


def get_total_ribbon(z):

    total_ribbon = 0
    pkg_regex = r"(\d+)x(\d+)x(\d+)"

    for pkg in re.findall(pkg_regex, z):

        # Get package dimensions as integers
        l = int(pkg[0])
        w = int(pkg[1])
        h = int(pkg[2])

        # Find smallest two sides (a & b)
        if h < w:
            a = h
            b = l if l < w else w
        else:
            a = w
            b = l if l < h else h

        # Calculate ribbon + bow for present and add to total
        total_ribbon += 2*a + 2*b + l*w*h

    return total_ribbon



# Benchmark functions and compare them to Cython implementations

if __name__ == "__main__":

    from time import process_time as time

    loop_count = 1000

    # Get solutions from all functions
    ans_p1 = get_total_wrapping(z)
    ans_p2 = get_total_ribbon(z)
    ans_p1_c = get_total_wrapping_c(z)
    ans_p2_c = get_total_ribbon_c(z)

    # Benchmark pure Python functions
    t1 = time()
    for i in range(loop_count):
        get_total_wrapping(z)
    t2 = time()
    for i in range(loop_count):
        get_total_ribbon(z)
    t3 = time()
    part1 = (t2 - t1) * 1000  # in ms
    part2 = (t3 - t2) * 1000  # in ms

    # Benchmark Cython functions
    t1 = time()
    for i in range(loop_count):
        get_total_wrapping_c(z)
    t2 = time()
    for i in range(loop_count):
        get_total_ribbon_c(z)
    t3 = time()
    part1_c = (t2 - t1) * 1000  # in ms
    part2_c = (t3 - t2) * 1000  # in ms

    # Report performance info & solutions
    template = "  - Part {0}: Solution = {1}, Time = {2} ms"
    print("")
    print("Pure Python Solutions ({0} loops):".format(loop_count))
    print(template.format(1, ans_p1, round(part1, 3)))
    print(template.format(2, ans_p2, round(part2, 3)))
    print("")
    print("Cython Solutions ({0} loops):".format(loop_count))
    print(template.format(1, ans_p1_c, round(part1_c, 3)))
    print(template.format(2, ans_p2_c, round(part2_c, 3)))
    print("")
