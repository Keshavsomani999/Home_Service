from django.contrib.auth.models import User, UserManager
from django.db import models


# Create your models here.


class Labours(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    phone_no = models.IntegerField()
    experience = models.IntegerField()
    total_project_done = models.IntegerField()
    Audio_visual = models.BooleanField(default=False)
    Electrical = models.BooleanField(default=False)
    Maintenance = models.BooleanField(default=False)
    Plumbing = models.BooleanField(default=False)
    Tiling = models.BooleanField(default=False)
    Wiring = models.BooleanField(default=False)
    arival_price = models.IntegerField()
    desc = models.TextField()
    total_certificate = models.IntegerField()
    certificate_1_name = models.CharField(max_length=500, blank=True)
    certificate_1_img = models.ImageField(upload_to='pics', blank=True)
    certificate_2_name = models.CharField(max_length=500, blank=True)
    certificate_2_img = models.ImageField(upload_to='pics', blank=True)
    certificate_3_name = models.CharField(max_length=500, blank=True)
    certificate_3_img = models.ImageField(upload_to='pics', blank=True)
    certificate_4_name = models.CharField(max_length=500, blank=True)
    certificate_4_img = models.ImageField(upload_to='pics', blank=True)
    Facebook_link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Labours"

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    subject = models.CharField(max_length=111)
    message = models.TextField(max_length=11111)

    class Meta:
        verbose_name_plural = "contact"

    def __str__(self):
        return self.name


class Orders(models.Model):
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    message = models.TextField(max_length=11111)
    labour = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip = models.IntegerField()
    phone = models.IntegerField()
    test = models.CharField(max_length=111)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "orders"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=111)
    desc = models.TextField(max_length=11111)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class ReviewRating(models.Model):
    product = models.ForeignKey(Labours, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject