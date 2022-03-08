class RocketEngine:

    count = 0
    all_power = 0

    @staticmethod
    def status():
        print(f"Number of engines: {RocketEngine.count}\nTotal power (powered engines only): {RocketEngine.all_power}")

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.working = False
        RocketEngine.count += 1

    def start(self):
        if not self.working:
            self.working = True
            RocketEngine.all_power += self.power

    def stop(self):
        if self.working:
            self.working = False
            RocketEngine.all_power -= self.power

    def __str__(self):
        return f"Engine name: {self.name}\nPower: {self.power}\nIs turned on: {self.working}"

    def __del__(self):
        if self.working:
            RocketEngine.all_power -= self.power
        RocketEngine.count -= 1
