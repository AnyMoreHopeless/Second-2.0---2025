class Car:
    def __init__(self, make: str, model: str, year: int, mileage: float) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} с пробегом {self.mileage} км"

    def __repr__(self) -> str:
        return f"Car(make={self.make}, model={self.model}, year={self.year}, mileage={self.mileage})"

    def drive(self, distance: float) -> None:
        self.mileage += distance
        print(f"{self.make} {self.model} проехал {distance} км.")


class Sedan(Car):
    def __init__(self, make: str, model: str, year: int, mileage: float, num_doors: int) -> None:
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors

    def __str__(self) -> str:
        return f"{super().__str__()} и {self.num_doors} дверями"

    def __repr__(self) -> str:
        return f"Sedan(make={self.make}, model={self.model}, year={self.year}, mileage={self.mileage}, num_doors={self.num_doors})"

    def drive(self, distance: float) -> None:
        super().drive(distance)
        print(f"Легковой автомобиль {self.make} {self.model} успешно преодолел {distance} км.")


class Truck(Car):
    def __init__(self, make: str, model: str, year: int, mileage: float, capacity: float) -> None:
        super().__init__(make, model, year, mileage)
        self.capacity = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} с грузоподъемностью {self.capacity} тонн"

    def __repr__(self) -> str:
        return f"Truck(make={self.make}, model={self.model}, year={self.year}, mileage={self.mileage}, capacity={self.capacity})"

    def drive(self, distance: float) -> None:
        super().drive(distance)
        print(f"Грузовой автомобиль {self.make} {self.model} успешно перевез {self.capacity} тонн на {distance} км.")
