import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    y = 0
    x = int(math.sqrt(sq))
    if x*x == sq:
        y = x+1
        return y*y
    return -1