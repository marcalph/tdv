


def two_number_sum(array, target_sum):
    viewed = set()
    for n in array:
        if target_sum-n in viewed:
            return [n, target_sum-n]
        else:
            viewed.add(target-n)
    return []