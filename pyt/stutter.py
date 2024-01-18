def stutter(string):
    if not string:
        return 'yeah okay buddy'
    else:
        splice_dat = string[:2]
        rest_dat = string[2:]
        return splice_dat + '...' + splice_dat + '...' + string