# Import required libraries

import os
from day1_c import get_floor_c, get_first_basement_c


# Read in input

with open('input', 'r') as f:
    z = f.read()


# Define pure Python functions for solving parts 1 & 2

def get_floor(z):
        
    floor = 0
    
    for bracket in z:
         floor += 1 if bracket == "(" else -1
         
    return floor


def get_first_basement(z):
        
    floor = 0
    pos = 0
      
    for bracket in z:
        pos += 1
        floor += 1 if bracket == "(" else -1
        if floor == -1:
            break
                        
    return pos


# Benchmark functions and compare them to Cython implementations

if __name__ == "__main__":
        
    from time import time
    
    loop_count = 1000
    
    # Get solutions from all functions
    ans_p1 = get_floor(z)
    ans_p2 = get_first_basement(z)
    ans_p1_c = get_floor_c(z)
    ans_p2_c = get_first_basement_c(z)
    
    # Benchmark pure Python functions
    t1 = time()
    for i in range(loop_count):
        get_floor(z)
    t2 = time()
    for i in range(loop_count):
        get_first_basement(z)
    t3 = time()
    part1 = (t2 - t1) * 1000  # in ms
    part2 = (t3 - t2) * 1000  # in ms
        
    # Benchmark Cython functions
    t1 = time()
    for i in range(loop_count):
        get_floor_c(z)
    t2 = time()
    for i in range(loop_count):
        get_first_basement_c(z)
    t3 = time()
    part1_c = (t2 - t1) * 1000  # in ms
    part2_c = (t3 - t2) * 1000  # in ms
        
    # Report performance info & solutions
    template = "  - Part {0}: Solution = {1}, Time = {2}"
    print("")
    print("Pure Python Solutions ({0} loops):".format(loop_count))
    print(template.format(1, ans_p1, part1))
    print(template.format(2, ans_p2, part2))
    print("")
    print("Cython Solutions ({0} loops):".format(loop_count))
    print(template.format(1, ans_p1_c, part1_c))
    print(template.format(2, ans_p2_c, part2_c))
    print("")
