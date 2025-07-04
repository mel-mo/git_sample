def recursive_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total
