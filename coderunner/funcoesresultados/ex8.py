def deivis_sequence(n, x=2, y=1, counter=0):
    if (counter < n - 2):
        x += y -1
        y = x - y + 1
        counter += 1
        return deivis_sequence(n, x, y, counter)
    else: 
        return x
