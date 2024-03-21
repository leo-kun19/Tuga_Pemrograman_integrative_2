class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

if __name__ == "__main__":
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    person = Person(weight, height)
    print("BMI:", person.BMI_Value())
