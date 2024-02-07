from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


REGION_CHOICES = [
    ('AN', 'Andijan'),
    ('BU', 'Bukhara'),
    ('FA', 'Fergana'),
    ('JI', 'Jizzakh'),
    ('XO', 'Khorezm'),
    ('NA', 'Namangan'),
    ('NW', 'Navoiy'),
    ('QA', 'Qashqadaryo'),
    ('SA', 'Samarkand'),
    ('SI', 'Sirdaryo'),
    ('SU', 'Surxondaryo'),
    ('TA', 'Tashkent'),
]


CAR_BRANDS = (
    ('Toyota', 'toyota_choices'),
    ('Honda', 'honda_choices'),
    ('Nissan', 'nissan_choices'),
    ('BMW', 'bmw_choices'),
    ('MercedesBenz', 'mercedes_benz_choices'),
    ('Audi', 'audi_choices'),
    ('Volkswagen', 'volkswagen_choices'),
    ('Lexus', 'lexus_choices'),
    ('Subaru', 'subaru_choices'),
    ('Mazda', 'mazda_choices'),
    ('Ford', 'ford_choices'),
    ('Chevrolet', 'chevrolet_choices'),
)


TYPE_OF_WATER_TRANSPORTS = [
    ('GIDRO', 'гидроцикл'),
    ('KATER', 'катер'),
    ('BOAT', 'лодка'),
    ('YAXTA', 'яхта'),
    ('ENGINE', 'лодочный мотор,двигатель')
]

TYPE_OF_MOTORCYCLES = [
    ('MOTO','мотоцикл'),
    ('MOPED','мопед'),
    ('SKUTER','скутер'),
    ('KVADRO','квадроцикл'),
    ('SNEGOXOD','снегоход'),
    ('PERSONAL','персональный транспортер'),
    ('AUTOPARTS','запчасти'),
    ('EQUIPMENT','экипировка'),
    ('OTHER','другой'),
]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WaterTypeCar(BaseModel):
    name = models.CharField(max_length=16, choices=TYPE_OF_WATER_TRANSPORTS)

    def __str__(self):
        return dict(TYPE_OF_WATER_TRANSPORTS).get(self.name, '')


class Toyota(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Honda(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Nissan(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class BMW(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class MercedesBenz(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Audi(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Volkswagen(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Lexus(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Subaru(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Mazda(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Ford(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Chevrolet(BaseModel):
    title = models.CharField(max_length=16)
    car_position = models.CharField(max_length=16, default='не указано')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
class CarModel(BaseModel):
    toyota = models.ForeignKey(Toyota, on_delete=models.CASCADE, related_name='toyota_passenger_cars')
    honda = models.ForeignKey(Honda, on_delete=models.CASCADE, related_name='honda_passenger_cars')
    nissan = models.ForeignKey(Nissan, on_delete=models.CASCADE, related_name='nissan_passenger_cars')
    bmw = models.ForeignKey(BMW, on_delete=models.CASCADE, related_name='bmw_passenger_cars')
    mercedes_benz = models.ForeignKey(MercedesBenz, on_delete=models.CASCADE, related_name='mercedes_benz_passenger_cars')
    audi = models.ForeignKey(Audi, on_delete=models.CASCADE, related_name='audi_passenger_cars')
    volkswagen = models.ForeignKey(Volkswagen, on_delete=models.CASCADE, related_name='volkswagen_passenger_cars')
    lexus = models.ForeignKey(Lexus, on_delete=models.CASCADE, related_name='lexus_passenger_cars')
    subaru = models.ForeignKey(Subaru, on_delete=models.CASCADE, related_name='subaru_passenger_cars')
    mazda = models.ForeignKey(Mazda, on_delete=models.CASCADE, related_name='mazda_passenger_cars')
    ford = models.ForeignKey(Ford, on_delete=models.CASCADE, related_name='ford_passenger_cars')
    chevrolet = models.ForeignKey(Chevrolet, on_delete=models.CASCADE, related_name='chevrolet_passenger_cars')



class PassengerCar(BaseModel):
    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    carbrands = models.CharField(max_length=16, choices=CAR_BRANDS)

    car_body = models.CharField(max_length=128)
    drive_unit = models.CharField(max_length=128)
    engine_type = models.CharField(max_length=128)
    transmission = models.CharField(max_length=128)
    mileage = models.IntegerField()
    color = models.CharField(max_length=128)
    search = models.TextField()

    is_bargain = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_leasetoown = models.BooleanField(default=False)

    price = models.IntegerField(
        validators=[
            MinValueValidator(2500),MaxValueValidator(6500)
        ]
    )
    year_of_issue = models.IntegerField(
        validators=[
            MinValueValidator(1900),MaxValueValidator(2024)
        ]
    )

class Motorcycles(BaseModel):
    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    motocycles = models.CharField(max_length=16, choices=TYPE_OF_MOTORCYCLES)

    search_field = models.TextField()

    is_bargain = models.BooleanField(default=False)

    price = models.IntegerField(
        validators=[
            MinValueValidator(2500),MaxValueValidator(6500)
        ]
    )
    year_of_issue = models.IntegerField(
        validators=[
            MinValueValidator(1900),MaxValueValidator(2024)
        ]
    )

class WaterTransport(BaseModel):
    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    water_type_transport = models.ForeignKey(WaterTypeCar, on_delete=models.CASCADE)

    search_field = models.TextField()

    is_bargain = models.BooleanField(default=False)

    price = models.IntegerField(
        validators=[
            MinValueValidator(2500),MaxValueValidator(6500)
        ]
    )


class Auto(BaseModel):
    passengercar = models.ForeignKey(PassengerCar, on_delete=models.CASCADE, related_name='passenger_car')
    motorcycles = models.ForeignKey(Motorcycles, on_delete=models.CASCADE, related_name='motor_cycles')
    watertransport = models.ForeignKey(WaterTransport, on_delete=models.CASCADE, related_name='watert_ransport')
