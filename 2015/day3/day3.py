# Import required libraries

from day3_c import get_visited_houses_c, get_visited_houses_robo_c



# Read in input

with open('input', 'r') as f:
    z = f.read()



# Define pure Python functions for solving parts 1 & 2    

def get_visited_houses(z):

    current_x = 0
    current_y = 0

    houses = {"0,0": True}
    for movement in z:
        if movement == "^":
            current_y += 1
        elif movement == "v":
            current_y -= 1
        elif movement == ">":
            current_x += 1
        elif movement == "<":
            current_x -= 1
        current_house = "%i,%i" % (current_x, current_y)
        houses[current_house] = True

    return len(houses)


def get_visited_houses_robo(z):

    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    houses = {"0,0": True}
    for i in range(len(z)):
        movement = z[i]
        if i % 2 == 0:
            if movement == "^":
                santa_y += 1
            elif movement == "v":
                santa_y -= 1
            elif movement == ">":
                santa_x += 1
            elif movement == "<":
                santa_x -= 1
            current_house = "%i,%i" % (santa_x, santa_y)
        else:
            if movement == "^":
                robo_y += 1
            elif movement == "v":
                robo_y -= 1
            elif movement == ">":
                robo_x += 1
            elif movement == "<":
                robo_x -= 1
            current_house = "%i,%i" % (robo_x, robo_y)
        houses[current_house] = True

    return len(houses)



# Benchmark functions and compare them to Cython implementations

if __name__ == "__main__":

    from time import process_time as time

    loop_count = 1000

    # Get solutions from all functions
    ans_p1 = get_visited_houses(z)
    ans_p2 = get_visited_houses_robo(z)
    ans_p1_c = get_visited_houses_c(z)
    ans_p2_c = get_visited_houses_robo_c(z)

    # Benchmark pure Python functions
    t1 = time()
    for i in range(loop_count):
        get_visited_houses(z)
    t2 = time()
    for i in range(loop_count):
        get_visited_houses_robo(z)
    t3 = time()
    part1 = (t2 - t1) * 1000  # in ms
    part2 = (t3 - t2) * 1000  # in ms

    # Benchmark Cython functions
    t1 = time()
    for i in range(loop_count):
        get_visited_houses_c(z)
    t2 = time()
    for i in range(loop_count):
        get_visited_houses_robo_c(z)
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
