#cython: language_level=3

import _md5


def get_smallest_adventcoin_num_sub_c(str z, int zeros, int start, int step):

    cdef int n = start

    zb = z.encode('utf8')
    zeros_str = "0" * zeros
    while True:
        hash = _md5.md5(b"%s%i" % (zb, n)).hexdigest()
        if hash[:zeros] == zeros_str:
            return n
        n = n + step
