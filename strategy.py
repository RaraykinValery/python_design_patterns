from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


mallard = MallardDuck()
mallard.perform_quack()
mallard.perform_fly()
