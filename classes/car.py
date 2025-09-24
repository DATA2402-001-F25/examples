
class Car:
    """
    Cars have maintenance schedule (days to next check), year, make, model
    """
    def __init__(self, maintenance_schedule: int, year: int, make: str, model: str):
        self.maint_sched = maintenance_schedule
        self.year = year
        self.make = make
        self.model = model
    
fleet = []

for car_number in range(2):
    make = input('enter car make')
    model = input('enter car model')
    year = int(input('enter car year'))
    sched = int(input('enter days to next tune-up'))
    this_car = Car(sched, year, make, model)
    fleet.append(this_car)

