from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display() -> None:
        pass


class WeatherData(Subject):
    def __init__(self) -> None:
        self.observers: list[Observer] = []
        self.temperature: float
        self.humidity: float
        self.pressure: float

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature: float
        self.humidity: float

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity"
        )


if __name__ == "__main__":
    weather_data = WeatherData()

    current_conditions_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
