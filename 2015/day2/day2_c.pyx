#cython: language_level=3

from libc.stdio cimport sscanf


def get_total_wrapping_c(str z):

    cdef int total_area = 0
    cdef int l, h, w, area
    cdef int a, b
    
    for pkg in z.encode('utf8').split(b"\n"):
        
        # Get package dimensions as integers
        if pkg == b"":
            break
        sscanf(pkg, "%dx%dx%d", &l, &h, &w)
        
        # Find smallest two sides (a & b)
        if h < w:
            a = h
            b = l if l < w else w
        else:
            a = w
            b = l if l < h else h
        
        # Calculate area + slack for present and add to total
        area = (2*l*w + 2*w*h + 2*h*l)
        total_area += area + a*b

    return total_area


def get_total_ribbon_c(str z):

    cdef int total_ribbon = 0
    cdef int l, h, w
    cdef int a, b
    
    for pkg in z.encode('utf8').split(b"\n"):
        
        # Get package dimensions as integers
        if pkg == b"":
            break
        sscanf(pkg, "%dx%dx%d", &l, &h, &w)
        
        # Find smallest two sides (a & b)
        if h < w:
            a = h
            b = l if l < w else w
        else:
            a = w
            b = l if l < h else h
        
        # Calculate ribbon + bow for present and add to total
        total_ribbon += 2*a + 2*b + l*h*w
        
    return total_ribbon
