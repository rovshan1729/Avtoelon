from django.db import models
from Cars.models import BaseModel

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

class Region(models.Model):
    name = models.CharField(max_length=16, choices=REGION_CHOICES)

    def __str__(self):
        return dict(REGION_CHOICES).get(self.name, '')
    

class SpareParts(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    search_field = models.TextField()
    
    search_from_text = models.BooleanField(default=False)

    with_photo = models.ImageField(upload_to='media/')
    is_bargain = models.BooleanField(default=False)

    price = models.IntegerField()

    CONDITION_CHOICES = (
        ('USED','б/у'),
        ('NEW','новые'),
    )
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)

class AutoPartsAndDeeds(BaseModel):
    spareparts = models.ForeignKey(SpareParts, on_delete=models.CASCADE)
