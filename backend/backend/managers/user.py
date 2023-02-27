from datetime import timedelta
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserQueryset(models.QuerySet):
    def filter_email_or_phone(self, email, phone):
        return self.filter(email=email) | self.filter(phone=phone)

    def filter_email(self, email):
        return self.filter(email=email)

    def filter_phone(self, phone):
        return self.filter(phone=phone)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset()

    def create_superuser(
        self, username, password, email=None, phone=None, **extra_fields
    ):
        """
        Special Manager method for createsuperuser command
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(
            username, password, email, phone, **extra_fields
        )

    def create_user(self, username, password, email, phone, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        NOTE: We can enforce database level business logic inside Manager methods
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.model.normalize_email(email)
        # phone = self.model.normalize_phone(phone)
        if not phone:
            phone = ""
        username = self.model.normalize_username(username)
        user = self.model(
            username=username, phone=phone, email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
