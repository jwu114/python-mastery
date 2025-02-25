def counter(n):
    def incr():
        n.append(1)
        return n
    return incr