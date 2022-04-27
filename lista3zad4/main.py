def gen_time(start_time: tuple, end_time: tuple, jump_time: tuple):
    yield start_time
    next_time = list(start_time)
    while next_time[0] <= end_time[0] or (next_time[1] <= end_time[1] and next_time[2] <= end_time[2]):
        if next_time[0] + jump_time[0] > 23:
            next_time[0] = (next_time[0] + jump_time[0]) % 24
        else:
            next_time[0] += jump_time[0]
        if next_time[1] + jump_time[1] > 59:
            next_time[1] = (next_time[1] + jump_time[1]) % 60
            next_time[0] += 1
        else:
            next_time[1] += jump_time[1]
        if next_time[2] + jump_time[2] > 59:
            next_time[2] = (next_time[2] + jump_time[2]) % 60
            next_time[1] += 1
        else:
            next_time[2] += jump_time[2]
        yield tuple(next_time)
        if next_time[0] + jump_time[0] >= end_time[0]:
            if next_time[1] + jump_time[1] >= end_time[1]:
                break


if __name__ == '__main__':
    for time in gen_time((8, 10, 00), (10, 50, 15), (0, 15, 12)):
        print(time)
