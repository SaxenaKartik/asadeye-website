from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self, name, email, phone_no, password = None):
        if not name:
            raise ValueError("User must have a name")

        email = self.normalize_email(email)
        user = self.model(name = name, email=email, phone_no = phone_no)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, phone_no, password):
        user = self.create_user(name, email, phone_no, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Model for users in the system"""
    name = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(max_length = 255)
    phone_no = PhoneNumberField(null = True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["email", "phone_no"]

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_no(self):
        return self.phone_no

    def __str__(self):
        return str(self.name) + " " + str(self.email) + " " + str(self.phone_no)

class Products(models.Model):
    """ Model for a products"""
    product_name = models.CharField(max_length = 100)
    product_price = models.FloatField()
    product_desc = models.CharField(max_length = 500)
    def __str__(self):
        return "name : " + str(self.product_name) + " price : " + str(self.product_price) + " description : " + str(self.product_desc)

    class Meta:
    	verbose_name_plural = "Products"


class Images(models.Model):
    """ Model for a images"""
    image_name = models.CharField(max_length = 500)
    path = models.FileField(upload_to = "images/")
    product_id = models.ForeignKey(Products, on_delete = models.CASCADE)
    def __str__(self):
        return  "id : " + str(self.id) + "name : " + str(self.image_name) +  "path : " + str(self.path) + "product_id : " + str(self.product_id)

    class Meta:
    	verbose_name_plural = "Images"
