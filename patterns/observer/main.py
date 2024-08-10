
from abc import ABC, ABCMeta, abstractmethod
import random
from typing import List


class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class ISubject(ABC):
    @abstractmethod
    def register(self, observer: IObserver):
        pass
    
    @abstractmethod
    def deregister(self, observer: IObserver):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class WeatherDataSubject(ISubject):
    __temperature: float = None
    __humidity: float = None
    __pressure: float = None
    
    def __init__(self) -> None:
        self.__observers: List[IObserver] = []
    
    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity
        
    @property
    def pressure(self):
        return self.__pressure
        
    @temperature.setter
    def temperature(self, value):
        self.__temperature = value
        self.notify()

    @humidity.setter
    def humidity(self, value):
        self.__humidity = value
        self.notify()
        
    @pressure.setter
    def pressure(self, value):
        self.__pressure = value
        self.notify()
        
    def register(self, observer: IObserver):
        self.__observers.append(observer)
    
    def deregister(self, observer: IObserver):
        self.__observers.remove(observer)
    
    def notify(self):
        print("+=========================**Notifying**=========================+")
        print()
        for observer in self.__observers:
            observer.update()
            
class WeatherConditions(IObserver):
    def __init__(self, subject: ISubject) -> None:
        self.subject = subject
        self.subject.register(self)
        
    def update(self):
        print("+---------------------------------------+")
        print("----- Current Weather Conditions --------")
        self.display()
    
    def display(self):
        current_temperature = f"{self.subject.temperature}°C" if self.subject.temperature is not None else "Data not Available."
        current_pressure = f"{self.subject.pressure}kPa" if self.subject.pressure is not None else "Data not Available."
        current_humidity = f"{self.subject.humidity}%" if self.subject.humidity is not None else "Data not Available."
        print(f"Temperature: {current_temperature}")
        print(f"Pressure: {current_pressure}")
        print(f"Humidity: {current_humidity}\n")
        
class ForecastConditions(IObserver):
    def __init__(self, subject: ISubject) -> None:
        self.subject = subject
        self.subject.register(self)
        
    def update(self):
        print("+---------------------------------------+")
        print("----- Forecasted Weather Conditions --------")
        self.display()
        
    def display(self):
        direction = ["+", "-"]
        random.shuffle(direction)
        
        temp_temperature = f"{self.subject.temperature} {direction[0]} {random.randint(0, 40)}"
        temp_pressure = f"{self.subject.pressure} {direction[0]} {random.randint(0, 100)}"
        temp_humidity = f"{self.subject.humidity} {direction[0]} {random.randint(0, 10)}"
        
        new_temperature = temp_temperature if self.subject.temperature is not None else self.subject.temperature
        new_pressure = temp_pressure if self.subject.pressure is not None else self.subject.pressure
        new_humidity = temp_humidity if self.subject.humidity is not None else self.subject.humidity
        
        forecasted_temperature = f"{eval(new_temperature)}°C" if new_temperature is not None else "Data not Available."
        forecasted_pressure = f"{eval(new_pressure)}kPa" if new_pressure is not None else "Data not Available."
        forecasted_humidity = f"{eval(new_humidity)}%" if new_humidity is not None else "Data not Available."
        
        print(f"Forecasted Temperature: {forecasted_temperature}")
        print(f"Forecasted Pressure: {forecasted_pressure}")
        print(f"Forecasted Humidity: {forecasted_humidity}")
        
        if self.subject.temperature is not None and eval(new_temperature) < 15:
            print("It's Going to be Cold.") 
        elif self.subject.temperature is not None and eval(new_temperature) > self.subject.temperature + 3:
            print("It's Going to be Hotter.")
        elif self.subject.temperature is not None and eval(new_temperature) < self.subject.temperature - 3:
            print("It's Going to be Colder.")
        else:
            print("Much of the Same.")
        
        print()
    
class WeatherStatistics(IObserver):
    def __init__(self, subject: ISubject) -> None:
        self.subject = subject
        self.subject.register(self)
        
    def update(self):
        print("+---------------------------------------+")
        print("----- Weather Statistics Conditions -----")
        self.display()
        
    def display(self):
        temp_temperature = f"{self.subject.temperature} - {random.randint(0, 40)}"
        temp_pressure = f"{self.subject.pressure} + {random.randint(0, 100)}"
        temp_humidity = f"{self.subject.humidity} / {random.randint(0, 10)}"
        
        new_temperature = temp_temperature if self.subject.temperature is not None else self.subject.temperature
        new_pressure = temp_pressure if self.subject.pressure is not None else self.subject.pressure
        new_humidity = temp_humidity if self.subject.humidity is not None else self.subject.humidity
        
        max_temperature = f"{eval(new_temperature)}°C" if new_temperature is not None else "Data not Available."
        min_pressure = f"{eval(new_pressure)}kPa" if new_pressure is not None else "Data not Available."
        ave_humidity = f"{eval(new_humidity)}%" if new_humidity is not None else "Data not Available."
        
        print(f"Maximum Temperature: {max_temperature}")
        print(f"Minimum Pressure: {min_pressure}")
        print(f"Average Humidity: {ave_humidity}\n")
        
# At Runtime
weather_subject = WeatherDataSubject()

WeatherConditions(weather_subject)
ForecastConditions(weather_subject)
WeatherStatistics(weather_subject)

# Updates from Weather Station
weather_subject.temperature = 0
weather_subject.pressure = 15
weather_subject.humidity = 30
