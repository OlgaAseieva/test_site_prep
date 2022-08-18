import uuid
import os
from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):

    slug = models.SlugField(max_length=50, db_index=True)
    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', 'is_visible',)
        index_together = (('id', 'slug'), )

class Menu(models.Model):

    def get_file_name (self, filename : str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'

        return os.path.join('menu/', new_filename)

    slug = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    ingrid = models.CharField(max_length=200)
    descript = models.TextField(max_length=500, default=True)
    price = models.DecimalField(max_digits= 8, decimal_places=2)
    special_dish = models.BooleanField(default=False)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)


    class Meta:
        ordering = ('is_visible', 'position')
        index_together = (('id', 'slug'), )

    def __str__(self):
        return f"{self.name}\n{self.ingrid} ________ {self.price} "




class Event(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'

        return os.path.join('event/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    descript = models.CharField(max_length=300)
    price = models.DecimalField(max_digits= 8, decimal_places=2)
    date_ev = models.DateField(auto_created=True)
    is_visible = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('is_visible', 'date_ev')

    def __str__(self):
        return f"{self.title}\n{self.date_ev}\n {self.descript}\n {self.price} "

class Galery (models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'

        return os.path.join('picture/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    descript = models.CharField(max_length=300)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.descript}'

#class Spesial (models.Model):
#    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)

class AboutUs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'

        return os.path.join('picture/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    descript = models.TextField(max_length=500)
    is_visible = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        ordering = ('is_visible', )

class WhyUs(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    descript = models.TextField(max_length=500)
    # is_visible = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ('is_visible', )

class UserReservation(models.Model):

    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, validators=[mobile_re])
    person = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=400, blank=True)
    plan_date = models.DateTimeField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    in_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-in_processed')

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.plan_date} {self.person} person \n {self.message[:100]}'


