# Generated by Django 4.1.5 on 2023-02-21 16:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created At"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Updated At"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, verbose_name="Is deleted instance"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="Is active instance"
                    ),
                ),
                (
                    "extra_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="Extra Data",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="name"
                    ),
                ),
            ],
            options={
                "verbose_name": "state",
                "verbose_name_plural": "states",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created At"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Updated At"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, verbose_name="Is deleted instance"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="Is active instance"
                    ),
                ),
                (
                    "extra_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="Extra Data",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="name"
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="location_state",
                        to="backend.state",
                        verbose_name="State",
                    ),
                ),
            ],
            options={
                "verbose_name": "location",
                "verbose_name_plural": "locations",
            },
        ),
        migrations.CreateModel(
            name="Area",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created At"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Updated At"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, verbose_name="Is deleted instance"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="Is active instance"
                    ),
                ),
                (
                    "extra_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="Extra Data",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="name"
                    ),
                ),
                (
                    "pincode",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="pincode"
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="area_location",
                        to="backend.location",
                        verbose_name="Location",
                    ),
                ),
            ],
            options={
                "verbose_name": "area",
                "verbose_name_plural": "area",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created At"
                    ),
                ),
                (
                    "updated_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Updated At"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, verbose_name="Is deleted instance"
                    ),
                ),
                (
                    "extra_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="Extra Data",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        help_text="Required. 128 characters or fewer.Letters, digits and @/./+/-/_ only.",
                        max_length=128,
                        unique=True,
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        db_index=True,
                        max_length=254,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                        verbose_name="phone number",
                    ),
                ),
                (
                    "country_code",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        null=True,
                        verbose_name="Country Code",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        max_length=1024,
                        null=True,
                        upload_to="",
                        verbose_name="Profile Image",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Un select this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date joined"
                    ),
                ),
                (
                    "is_phone_verified",
                    models.BooleanField(
                        default=False, verbose_name="Is Phone Verified"
                    ),
                ),
                (
                    "is_email_verified",
                    models.BooleanField(
                        default=False, verbose_name="Is Email Verified"
                    ),
                ),
                (
                    "is_gmail_login",
                    models.BooleanField(
                        default=False, verbose_name="Is Gmail Login"
                    ),
                ),
                (
                    "password_updated_on",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Password Updated On",
                    ),
                ),
                (
                    "failed_login_attempts",
                    models.PositiveSmallIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinLengthValidator(0),
                            django.core.validators.MaxValueValidator(10),
                        ],
                        verbose_name="No of Failed Login Attempts",
                    ),
                ),
                (
                    "failed_login_time",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Last failed login attempt time",
                    ),
                ),
                (
                    "current_address",
                    models.TextField(
                        blank=True, verbose_name="current address"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[("Admin", "Admin"), ("User", "User")],
                        max_length=128,
                        verbose_name="role",
                    ),
                ),
                (
                    "email_otp",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxValueValidator(6),
                        ],
                        verbose_name="Email OTP",
                    ),
                ),
                (
                    "phone_otp",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinLengthValidator(6),
                            django.core.validators.MaxValueValidator(6),
                        ],
                        verbose_name="Phone OTP",
                    ),
                ),
                (
                    "email_expiry",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Email Expiry"
                    ),
                ),
                (
                    "phone_expiry",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Phone Expiry"
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_area",
                        to="backend.area",
                        verbose_name="Area",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
    ]
