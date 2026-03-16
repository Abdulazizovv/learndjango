from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


def validate_number(value: str):
    if not value.startswith("+998"):
        raise ValidationError("Telefon raqam +998 bilan boshlanishi kerak")
    
    if len(value) < 12 or len(value) > 14:
        raise ValidationError("Uzunlik 13 bo'lishi kerak")
    
    if not value.split("+998")[1].isdigit():
        raise ValidationError("Faqat raqamlardan tashkil topgan bo'lishi kerak!")



class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise ValidationError("Telefon raqam majburiy")
        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password, **kwargs):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(AbstractUser):
    first_name = None
    last_name = None

    phone_number = models.CharField(max_length=15, validators=[validate_number], unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.phone_number