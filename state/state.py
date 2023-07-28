class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    state = SOLD_OUT
    count = 0

    def __init__(self, count):
        self.count = count
        if self.count > 0:
            self.state = self.NO_QUARTER

    def __str__(self):
        return ("\nMighty Gumball, Inc.\n"
                "Python-enabled Standing Gumball Model #2004\n"
                f"Inventory: {self.count} gumballs\n")

    def insert_quarter(self):
        if self.state == self.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == self.SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self.state == self.SOLD:
            print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        if self.state == self.HAS_QUARTER:
            print("Quarter returned")
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You haven't inserted a quarter")
        elif self.state == self.SOLD:
            print("Sorry, you already turned the crank")
        elif self.state == self.SOLD_OUT:
            print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self):
        if self.state == self.SOLD:
            print("Turning twice doesn't get you another gumball!")
        elif self.state == self.NO_QUARTER:
            print("You turned but there's no quarter")
        elif self.state == self.SOLD_OUT:
            print("You turned, but there are no gumballs")
        elif self.state == self.HAS_QUARTER:
            print("You turned...")
            self.state = self.SOLD
            self.dispense()

    def dispense(self):
        if self.state == self.SOLD:
            print("A gumball comes rolling out the slot")
            self.count = self.count - 1
            if self.count == 0:
                print("Oops, out of gumballs!")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You need to pay first")
        elif self.state == self.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == self.HAS_QUARTER:
            print("You need to turn the crank")


gumball_machine = GumballMachine(5)

print(gumball_machine)
gumball_machine.insert_quarter()
gumball_machine.turn_crank()

print(gumball_machine)
gumball_machine.insert_quarter()
gumball_machine.eject_quarter()
gumball_machine.turn_crank()

print(gumball_machine)
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.insert_quarter()
gumball_machine.turn_crank()
gumball_machine.eject_quarter()

print(gumball_machine)
