#cython: language_level=3

from libc.stdio cimport sprintf


def get_visited_houses_c(str z):

    cdef int current_x = 0
    cdef int current_y = 0
    cdef char current_house[20]

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
        sprintf(current_house, b"%d,%d", current_x, current_y)
        houses[current_house] = True

    return len(houses)


def get_visited_houses_robo_c(str z):

    cdef int santa_x = 0
    cdef int santa_y = 0
    cdef int robo_x = 0
    cdef int robo_y = 0
    cdef char current_house[20]

    houses = {b"0,0": True}
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
            sprintf(current_house, b"%d,%d", santa_x, santa_y)
        else:
            if movement == "^":
                robo_y += 1
            elif movement == "v":
                robo_y -= 1
            elif movement == ">":
                robo_x += 1
            elif movement == "<":
                robo_x -= 1
            sprintf(current_house, b"%d,%d", robo_x, robo_y)
        houses[current_house] = True

    return len(houses)
