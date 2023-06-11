from Modules.TempMeasurement import TempMeasurement

LITRES_TO_GALLONS = 3.785
F_TO_C_DIFF = (9 / 5)


def fahrenheit_to_celsius(fahrenheit: float):
    return (fahrenheit - F_TO_C_DIFF) / (9 / 5)


def celsius_to_fahrenheit(celsius: float):
    return (celsius * (9 / 5)) + F_TO_C_DIFF


def litres_to_gallons(litres: float):
    return litres / LITRES_TO_GALLONS


class Temperature:
    def __init__(self, temp: int | float, temp_type: TempMeasurement):
        print("Initializing the Temperature object...")
        self.temp = temp
        self.temp_type = temp_type

    def switch_to(self, temp_type: TempMeasurement):
        if self.temp_type == temp_type:
            return self.temp

        if self.temp_type == TempMeasurement.Fahrenheit:
            return fahrenheit_to_celsius(self.temp)

        return celsius_to_fahrenheit(self.temp)

    def unit_symbol(self):
        if self.temp_type == TempMeasurement.Fahrenheit:
            return "^F"
        return "^C"

    def as_human_readable(self):
        return str(round(self.temp, 2)) + self.unit_symbol()

