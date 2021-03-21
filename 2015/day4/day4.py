# Import required libraries

import os
import _md5
import multiprocessing as mp

from day4_c import get_smallest_adventcoin_num_sub_c


# Define puzzle input

z = "iwrupvqb"


# Define pure Python functions for solving parts 1 & 2

def queue_wrap(func, args, q):
    result = func(*args)
    q.put(result)


def get_smallest_adventcoin_num_sub(z, zeros, start, step):

    n = start
    z = z.encode('utf8')
    zeros_str = "0" * zeros

    while True:
        hash = _md5.md5(b"%s%i" % (z, n)).hexdigest()
        if hash[:zeros] == zeros_str:
            return n
        n = n + step


def get_smallest_adventcoin_num(z, zeros = 5, use_c = False):

    # Initialize multiprocessing stuff
    jobs = []
    cores = os.cpu_count()
    result_q = mp.Queue()

    # Determine which subfunction to use
    if use_c:
        subfunc = get_smallest_adventcoin_num_sub_c
    else:
        subfunc = get_smallest_adventcoin_num_sub

    # Create and start individual adventcoin processes
    for i in range(cores):
        wrap_args = (
            subfunc,                   # function
            (z, zeros, i + 1, cores),  # arguments
            result_q                   # result queue
        )
        p = mp.Process(target = queue_wrap, args = wrap_args)
        p.start()
        jobs.append(p)

    # Wait for one of the processes to get the result
    while True:
        if not result_q.empty():
            for p in jobs:
                p.terminate()
            break

    return result_q.get()


# Benchmark functions and compare them to Cython implementations

if __name__ == "__main__":

    from time import process_time as time

    loop_count = 2

    # Benchmark pure Python functions
    t1 = time()
    for i in range(loop_count):
        ans_p1 = get_smallest_adventcoin_num(z, 5)
    t2 = time()
    for i in range(loop_count):
        ans_p2 = get_smallest_adventcoin_num(z, 6)
    t3 = time()
    part1 = (t2 - t1) * 1000  # in ms
    part2 = (t3 - t2) * 1000  # in ms

    # Benchmark Cython functions
    t1 = time()
    for i in range(loop_count):
        ans_p1_c = get_smallest_adventcoin_num(z, 5, use_c = True)
    t2 = time()
    for i in range(loop_count):
        ans_p2_c = get_smallest_adventcoin_num(z, 6, use_c = True)
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
