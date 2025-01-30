class Solution:
    def convertTemperature(self, Celsius: float) -> List[float]:
        kelvin = Celsius + 273.15
        fah = Celsius * 1.80 + 32.00
        return kelvin , fah