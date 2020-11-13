def decToHex(decimal, length=None):
    if length == 6:
        return '%06x' % int(decimal)

    if length == 4:
        return '%04x' % int(decimal)

    if length == 2:
        return '%02x' % int(decimal)

    return '%x' % int(decimal)
