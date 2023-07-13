# The Factory Method Pattern defines an interface
# for creating an object, but lets subclasses decide which
# class to instantiate. Factory Method lets a class defer
# instantiation to subclasses.

from abc import ABC, abstractmethod


def main():
    nyStore = NYPizzaStore()
    nyStore.order_pizza("cheese")


class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        print("Prepare " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print("   " + topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cut the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name

    def to_string(self):
        display = []
        display.append("---- " + self.name + " ----\n")
        display.append(self.dough + "\n")
        display.append(self.sauce + "\n")
        for topping in self.toppings:
            display.append(topping + "\n")
        return "".join(display)


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings.append("Grated Reggiano Cheese")


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, item):
        pass

    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        print("--- Making a " + pizza.get_name() + " ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == "cheese":
            return NYStyleCheesePizza()


if __name__ == "__main__":
    main()
