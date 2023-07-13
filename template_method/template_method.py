# The Template Method Pattern defines the skeleton
# of an algorithm in a method, deferring some steps to
# subclasses. Template Method lets subclasses redefine
# certain steps of an algorithm without changing the
# algorithm’s structure.

from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def add_condiments(self):
        print("Adding Sugar and Milk")


if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("\nMaking tea...")
    tea.prepare_recipe()

    print("\nMaking coffee...")
    coffee.prepare_recipe()
