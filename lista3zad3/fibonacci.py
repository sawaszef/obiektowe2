class Fibonacci:

    def __init__(self, limit):
        self.fibo_numbers = self.calc_fibo(limit)

    def calc_fibo(self, limit):
        fibo_list = [1, 1, 2]
        for n in range(3, limit):
            next_number = fibo_list[-1] + fibo_list[-2]
            fibo_list.append(next_number)
        return fibo_list

    def print_fibo(self):
        fibo_iter = iter(self.fibo_numbers)
        for _ in range(len(self.fibo_numbers)):
            print(next(fibo_iter))

