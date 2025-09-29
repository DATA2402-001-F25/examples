class Person:

    def __init__(self, name:str, email: str):
        self.name = name
        self.email = email
    
    def __repr__(self) -> str:
        return f'{self.name} ({self.email})'


class Car:
    """
    Cars have maintenance schedule (days to next check), year, make, model
    """
    def __init__(self, maintenance_schedule: int, year: int, make: str, model: str,
                odometer: int, owner: Person
    ):
        self.maint_sched = maintenance_schedule
        self.year = year
        self.make = make
        self.model = model
        self.odo = odometer
        self.owner = owner
    
    def tuneup(self):
        self.maint_sched = 30
    
    def drive(self, distance: int):
        self.odo += distance
        self.maint_sched -= 1
        self.maint_sched = max(self.maint_sched, 0)

    def __repr__(self) -> str:
        return f'{self.year} {self.make} {self.model} with {self.odo} km owned by {self.owner}'


me = Person('eric', 'echalmers@mtroyal.ca')
my_car = Car(0, 1983, 'GMC', "Sierra", 600_000, me)

print(my_car)