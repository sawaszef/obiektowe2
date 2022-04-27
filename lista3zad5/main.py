def prime_nums_gen():
    yield 2
    number = 3
    while True:
        is_prime = True
        for denominator in range(round(number / 2), 1, -1):
            if number % denominator == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1



if __name__ == '__main__':
    with open("prime_numbers.txt", 'a') as file:
        index = 0
        for n in prime_nums_gen():
            if index > 9999:
                break
            file.write(str(n) + "\n")
            index += 1


