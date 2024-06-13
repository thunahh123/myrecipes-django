from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser , UserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError ("An email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
     
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first = models.CharField(max_length=64, default="")
    last = models.CharField(max_length=64,  default="")
    username = models.CharField(max_length=64, default="", unique=True)
    email = models.EmailField(default="", unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def get_full_name(self):
        return self.username 
    def get_short_name(self):
        return self.first or self.username
    def __str__(self):
        return f"{self.first} {self.last} {self.email}"
    
