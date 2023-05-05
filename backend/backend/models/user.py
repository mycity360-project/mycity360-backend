# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.core.validators import (
    RegexValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from .area import Area
from ..managers.user import UserManager, UserQueryset
from gdstorage.storage import GoogleDriveStorage
from ..utils.services import get_file_path

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.",
)


class User(AbstractBaseUser, PermissionsMixin, Core):
    """
    Description of User Model
    """

    username = models.CharField(
        _("username"),
        max_length=128,
        unique=True,
        help_text=_(
            "Required. 128 characters or fewer."
            "Letters, digits and @/./+/-/_ only."
        ),
    )
    first_name = models.CharField(_("first name"), max_length=128, blank=True)
    last_name = models.CharField(_("last name"), max_length=128, blank=True)
    email = models.EmailField(_("email address"), blank=True, db_index=True)
    phone = models.CharField(
        _("phone number"),
        max_length=17,
        blank=True,
        validators=[phone_regex],
        db_index=True,
    )
    country_code = models.CharField(
        verbose_name=_("Country Code"), max_length=16, null=True, blank=True
    )
    profile_image = models.URLField(_("Image"), null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Un select this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_phone_verified = models.BooleanField(
        _("Is Phone Verified"), default=False
    )
    is_email_verified = models.BooleanField(
        _("Is Email Verified"), default=False
    )
    is_gmail_login = models.BooleanField(_("Is Gmail Login"), default=False)
    password_updated_on = models.DateTimeField(
        _("Password Updated On"), default=timezone.now
    )
    failed_login_attempts = models.PositiveSmallIntegerField(
        verbose_name=_("No of Failed Login Attempts"),
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    failed_login_time = models.DateTimeField(
        verbose_name=_("Last failed login attempt time"), null=True, blank=True
    )
    area = models.ForeignKey(
        verbose_name=_("Area"),
        to=Area,
        related_name="user_area",
        on_delete=models.SET_NULL,
        null=True,
    )
    current_address = models.TextField(_("current address"), blank=True)
    role = models.CharField(
        _("role"),
        max_length=128,
        blank=True,
        choices=(
            ("Admin", "Admin"),
            ("User", "User"),
        ),
    )
    email_otp = models.PositiveIntegerField(
        verbose_name=_("Email OTP"),
        validators=[MinValueValidator(111111), MaxValueValidator(999999)],
        null=True,
        blank=True,
    )
    phone_otp = models.PositiveIntegerField(
        verbose_name=_("Phone OTP"),
        validators=[MinValueValidator(111111), MaxValueValidator(999999)],
        null=True,
        blank=True,
    )
    email_expiry = models.DateTimeField(
        _("Email Expiry"), null=True, blank=True
    )
    phone_expiry = models.DateTimeField(
        _("Phone Expiry"), null=True, blank=True
    )

    objects = UserManager.from_queryset(UserQueryset)()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "backend"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return "phone: {} - email: {}".format(self.phone, self.email)

    def __unicode__(self):
        return "phone: {} - email {}".format(self.phone, self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by removing spaces and lowercasing it.
        """
        return email.strip().lower() if email else ""

    def check_password(self, password):
        """
        Check password and lockout user if number of attempts exceed.
        Returns:
        """
        is_correct_password = super(User, self).check_password(password)
        return is_correct_password
