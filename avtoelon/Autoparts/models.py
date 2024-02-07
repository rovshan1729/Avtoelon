from django.db import models
from Cars.models import BaseModel,CAR_BRANDS,CarModel

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

CONDITION_CHOICES = (
        ('USED','б/у'),
        ('NEW','новые'),
    )

SEASON = [
    ('SUM','Летние'),
    ('WIN','Зимние'),
    ('ALL','Все сезоны'),
]

TYPE_OF_DISK = [
    ('LEGKO','Легкосплавные'),
    ('STEEL','Стальные'),
]

class AutoAndAutopart(BaseModel):
    search_field = models.TextField()

    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES)
    carbrand = models.CharField(max_length=16, choices=CAR_BRANDS)

    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)


    price = models.IntegerField()

    is_bargain = models.BooleanField(default=False)
    with_photo = models.ImageField(upload_to='media/')



class Disk(BaseModel):
    search_field = models.TextField()

    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    disk_type = models.CharField(max_length=16, choices=TYPE_OF_DISK)

    size_width = models.FloatField()
    size_fasteners = models.CharField(max_length=16)

    price = models.IntegerField()

    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES)

    is_bargain = models.BooleanField(default=False)


class Tire(BaseModel):
    search_field = models.TextField()

    size_width = models.FloatField()
    size_profile = models.FloatField()
    size_diametr = models.IntegerField()

    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    season = models.CharField(max_length=16, choices=SEASON)

    price = models.IntegerField()

    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES)

    is_bargain = models.BooleanField(default=False)


class AccessoriesAndElectronics(BaseModel):
    search_field = models.TextField()

    region = models.CharField(max_length=16, choices=REGION_CHOICES)

    price = models.IntegerField()

    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES)

    is_bargain = models.BooleanField(default=False)



class ConsumablesAndOil(BaseModel):
    search_field = models.TextField()

    region = models.CharField(max_length=16, choices=REGION_CHOICES)

    price = models.IntegerField()

    condition = models.CharField(max_length=16, choices=CONDITION_CHOICES)

    is_bargain = models.BooleanField(default=False)





class SpareParts(BaseModel):
    region = models.CharField(max_length=16, choices=REGION_CHOICES)
    carbrands = models.CharField(max_length=16, choices=CAR_BRANDS)

    carmodel = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    search_field = models.TextField()

    search_from_text = models.BooleanField(default=False)

    with_photo = models.ImageField(upload_to='media/')
    is_bargain = models.BooleanField(default=False)

    price = models.IntegerField()

    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)

class AutoPartsAndDeeds(BaseModel):
    spareparts = models.ForeignKey(SpareParts, on_delete=models.CASCADE)
