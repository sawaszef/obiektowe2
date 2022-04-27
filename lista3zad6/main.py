def converter(sequence):
    if hasattr(sequence, "__iter__") and not isinstance(sequence, str):
        for collection in sequence:
            yield from converter(collection)
    else:
        yield sequence


if __name__ == '__main__':

    test = ([1, 'kot'], 3, (4, 5, [7, 8, 9]))
    seq = []

    for item in converter(test):
        seq.append(item)
    print(seq)
