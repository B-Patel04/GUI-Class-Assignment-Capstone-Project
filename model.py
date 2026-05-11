# model.py

class TemperatureModel:

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def validate_input(self, text):

        if not text.strip():
            return False, "Please enter a value."

        try:
            value = float(text)
        except ValueError:
            return False, "Input must be numeric."

        return True, value