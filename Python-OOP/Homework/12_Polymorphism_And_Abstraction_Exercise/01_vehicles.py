from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    AIR_CONDITION_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITION_CONSUMPTION) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel

    def __repr__(self):
        return f"Car: {self.fuel_quantity:.2f} liters"


class Truck(Vehicle):
    AIR_CONDITION_CONSUMPTION = 1.6
    REFUEL_EFFICIENCY = 0.95

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        total_consumption = (self.fuel_consumption + self.AIR_CONDITION_CONSUMPTION) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY

    def __repr__(self):
        return f"Truck: {self.fuel_quantity:.2f} liters"
