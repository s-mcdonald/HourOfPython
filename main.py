# Import the local and external libraries
from Modules import Converter, BasicCalculator as Calc
from Modules.Converter import TempMeasurement

if __name__ == '__main__':
    print(Calc.add(5, 3))
    print(Calc.sub(5, 3))
    print(Calc.mul(5, 3))
    print(Calc.div(5, 3))
    print(Converter.fahrenheit_to_celsius(85))
    print(Converter.celsius_to_fahrenheit(20))

    forty_five_c = Converter.Temperature(45, TempMeasurement.Celsius)
    ninety_five_f = Converter.Temperature(95, TempMeasurement.Fahrenheit)

    print(
        forty_five_c.switch_to(TempMeasurement.Fahrenheit),
        forty_five_c.unit_symbol()
    )

    print(
        ninety_five_f.switch_to(TempMeasurement.Celsius),
        ninety_five_f.unit_symbol()
    )

    print(ninety_five_f.as_human_readable())
