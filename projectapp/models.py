from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]
        ordering = ['id', 'name']


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id'])
        ]


class Address(models.Model):
    name = models.CharField(max_length=40)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id', 'name'])
        ]


class SellType(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
        indexes = [
            models.Index(fields=['id', 'name'])
        ]


class Apartment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    sell_type = models.ForeignKey(SellType, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=50)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    square = models.IntegerField()
    seller_phone = models.CharField(max_length=20)
    seller_name = models.CharField(max_length=30)
    price = models.FloatField()
    rooms = models.IntegerField()
    count_bath = models.IntegerField()
    count_floor = models.IntegerField()
    count_bedrooms = models.IntegerField()
    build_date = models.DateField(auto_now=True)
    reconstruct_date = models.DateField(auto_now=True)
    views = models.IntegerField()
    photo1 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo4 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo5 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo6 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo7 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo8 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo9 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)
    photo10 = models.ImageField(upload_to='media/apartment/photos/', null=True, blank=True)

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ['id', 'short_name']
        indexes = [
            models.Index(fields=['id', 'short_name', 'photo1'])
        ]


