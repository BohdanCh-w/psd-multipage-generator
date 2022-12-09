'''strings helper functions'''


def compact_str_list(*vals: list[str]) -> str:
    '''
    compact list of strings that represent numbers

    Example:
    - '01', '02', '03' -> '01-03'
    - '01', '02', '04' -> '01,02,04'
    - '01', '02', '03', '04', '07', '08', '09' -> '01-04,07-09'
    - '01', '02', '03', '05', '08', '09', '10' -> '01-03,05,08-10'
    '''
    if len(vals) < 3:
        return ','.join(vals)

    try:
        nums = tuple(map(int, vals))
    except ValueError:
        return ','.join(vals)
    
    groups = []
    start = 0
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i] - 1:
            continue
        groups.append(vals[start:i])
        start = i
    groups.append(vals[start:])

    return ','.join((gr[0] + '-' + gr[-1] if len(gr) > 2 else ','.join(gr) for gr in groups))
