def get_floor_c(str z):

    cdef int floor = 0

    for bracket in z:
        if bracket == "(":
            floor += 1
        else:
            floor -= 1

    return floor


def get_first_basement_c(str z):

    cdef int floor = 0
    cdef int pos = 0

    for bracket in z:
        pos += 1
        if bracket == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            break

    return pos
