def datetime_format(value, format='%H:%M / %d-%m-%Y'):
    if value is not None:
        return value.strftime(format)
    else:
        return ''
