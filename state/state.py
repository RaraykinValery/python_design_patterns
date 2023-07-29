from abc import ABC, abstractmethod


class GumballMachine:
    count = 0

    def __init__(self, number_gumballs: int):
        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)

        self.count = number_gumballs
        if self.count > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def __str__(self):
        return ("\nMighty Gumball, Inc.\n"
                "Python-enabled Standing Gumball Model #2004\n"
                f"Inventory: {self.count} gumballs\n")

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count = self.count - 1

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_count(self):
        return self.count


class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(
            self.gumball_machine.getHasQuarterState())

    def eject_quarter(self):
        print("You haven't inserted a quater")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't inserted another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(
            self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(
            self.gumball_machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")


class SoldState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(
                self.gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(
                self.gumball_machine.get_sold_out_state())


class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert quarter. There are no more gumballs")

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned crank, but there are no gumballs")

    def dispense(self):
        print("No qumballs dispensed")


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
