def filter_suppress_none(val):
    if val is not None:
        return val
    else:
        return ''
