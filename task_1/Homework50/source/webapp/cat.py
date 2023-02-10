from random import random


class Cat:
    name = ''
    health = 10
    happiness = 10
    satiety = 10
    rage = False
    state = ''
    sleep = ''

    def play(self):
        self.happiness += 15
        self.satiety -= 10
        self.state = 'Кот играет'
        if random() < 0.3:
            self.happiness = 0

    def feed(self):
        self.state = 'Кот кушает'
        self.happiness += 5
        self.satiety += 15
        if self.satiety >= 100:
            self.happiness -= 30

    def sleep(self):
        self.state = 'Кот спит'
