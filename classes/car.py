
class Car:
    """
    Cars have maintenance schedule (days to next check), year, make, model
    """
    def __init__(self, maintenance_schedule: int, year: int, make: str, model: str,
                odometer: int
    ):
        self.maint_sched = maintenance_schedule
        self.year = year
        self.make = make
        self.model = model
        self.odo = odometer
    
    def tuneup(self):
        self.maint_sched = 30
    
    def drive(self, distance: int):
        self.odo += distance
        self.maint_sched -= 1
        self.maint_sched = max(self.maint_sched, 0)

    def __repr__(self) -> str:
        return f'{self.year} {self.make} {self.model} with {self.odo} km'

fleet = []

# a loop that gets car details from user, and creates a Car object for each
# for car_number in range(2):
#     make = input('enter car make')
#     model = input('enter car model')
#     year = int(input('enter car year'))
#     sched = int(input('enter days to next tune-up'))
#     this_car = Car(sched, year, make, model)
#     fleet.append(this_car)


fleet = [
    Car(0, 1983, 'gmc', 'sierra', 1000),
    Car(30, 2010, 'porche', 'gt3 911', 1000),
    Car(4, 1968, 'wayne', 'batmobile', 1000)
]

for car in fleet:
    if car.maint_sched <= 5:
        print(car.make, car.model, car.year, 'needs maintenance this week')


# use the car's methods
my_car = Car(0, 1983, 'GMC', "Sierra", 600_000)
print(my_car.odo, my_car.maint_sched)
my_car.drive(100)
print(my_car.odo, my_car.maint_sched)

print(my_car)