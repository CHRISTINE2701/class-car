class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        """Display the details of the car."""
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}")

    def update_color(self, new_color):
        """Update the color of the car."""
        self.color = new_color
        print(f"The color of the car has been updated to: {self.color}")


# Task 2: Instantiate multiple objects of the Car class
car1 = Car("Toyota", "Corolla", 2020, "Blue")
car2 = Car("Honda", "Civic", 2019, "Red")
car3 = Car("Ford", "Mustang", 2021, "Black")

# Display the details of each car
car1.display_details()
car2.display_details()
car3.display_details()

# Update the color of one car object and display updated details
car1.update_color("Green")
car1.display_details()


# Task 3: Create a simple program to input details for a new car
def create_car_from_input():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    color = input("Enter car color: ")

    new_car = Car(make, model, year, color)
    print("\nNew Car Created:")
    new_car.display_details()


# Initiating the car creation process from user input
create_car_from_input()
