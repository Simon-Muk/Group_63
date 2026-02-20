class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        if self.unit == "cm":
            return self.value / 100
        elif self.unit == "m":
            return self.value
        elif self.unit == "km":
            return self.value * 1000

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        return Distance(total_meters, "m")

d1 = Distance(26, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)
print(d3)

result = d1 + d2
print("Сумма:", result)