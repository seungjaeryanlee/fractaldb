def dict_without(d, key):
    """Create new dict without one key."""
    new_d = d.copy()
    new_d.pop(key)

    return new_d
