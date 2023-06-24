from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models.user import User
from .models.area import Area
from .models.state import State
from .models.location import Location
from .models.system_config import SystemConfig
from .models.category import Category
from .models.user_ad import UserAd
from .models.saved_ad import SavedAd
from .models.service import Service
from .models.image import Image
from .models.question import Question
from .models.answer import Answer
from .models.banner import Banner
from .utils.admin import CustomModelAdmin


class ParentCategoryListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Parent Category")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "decade"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        category = Category.objects.filter(category__isnull=True)
        return [(cat.id, cat.name) for cat in category]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        if self.value():
            return queryset.filter(category_id=self.value())


class AreaAdmin(CustomModelAdmin):
    list_display = ("pk", "name", "pincode")
    search_fields = ("name", "location__name")
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        "location__name",
    )
    ordering = ("is_deleted", "is_active")


class UserAdmin(CustomModelAdmin):
    list_display = ("pk", "email", "phone", "first_name", "last_name")
    search_fields = ("email", "phone", "first_name", "last_name")
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        "area__name",
    )
    ordering = ("is_deleted", "is_active")


class StateAdmin(CustomModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    list_filter = ("is_active", "is_deleted", "created_date", "updated_date")
    ordering = ("is_deleted", "is_active")


class LocationAdmin(CustomModelAdmin):
    list_display = ("pk", "name")
    search_fields = (
        "name",
        "state__name",
    )
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        "state__name",
    )
    ordering = ("is_deleted", "is_active")


class SystemConfigAdmin(CustomModelAdmin):
    list_display = ("pk", "key", "value")
    search_fields = ("name", "key")
    list_filter = ("is_active", "is_deleted", "created_date", "updated_date")
    ordering = ("is_deleted", "is_active")


class CategoryAdmin(CustomModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["category"].queryset = Category.objects.filter(
            category__isnull=True
        )
        return form

    list_display = ("pk", "name", "sequence")
    search_fields = ("name",)
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        ParentCategoryListFilter,
    )
    ordering = ("is_deleted", "is_active")


class UserAdAdmin(CustomModelAdmin):
    list_display = (
        "pk",
        "name",
        "code",
        "is_featured",
        "price",
    )
    list_editable = ("is_featured",)
    search_fields = ("name", "user__email", "user__phone", "code")
    list_filter = (
        ("is_active", admin.BooleanFieldListFilter),
        "is_deleted",
        "created_date",
        "updated_date",
        "area",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
        "name",
        "description",
        "code",
        "tags",
        "images",
        "price",
        "category",
        "user",
        "area",
        "extra_data"
    )
    ordering = ("is_deleted", "is_active")


class ServiceAdmin(CustomModelAdmin):
    list_display = ("pk", "name", "sequence")
    search_fields = ("name", "code")
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
    )
    ordering = ("is_deleted", "is_active")


class ImageAdmin(CustomModelAdmin):
    list_display = ("pk", "image")
    # search_fields = ("name", "code")
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
    )
    ordering = ("is_deleted", "is_active")


class QuestionAdmin(CustomModelAdmin):
    list_display = ("pk", "question", "field_type", "category")
    search_fields = ("question", "category__name")
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        "category__name",
    )
    ordering = ("is_deleted", "is_active")


class AnswerAdmin(CustomModelAdmin):
    list_display = ("pk", "answer", "question")
    search_fields = (
        "answer",
        "question__question",
    )
    list_filter = ("is_active", "is_deleted", "created_date", "updated_date")
    ordering = ("is_deleted", "is_active")


class BannerAdmin(CustomModelAdmin):
    list_display = ("pk", "area", "redirect_url", "image")
    search_fields = (
        "area__name",
        "redirect_url",
    )
    list_filter = (
        "is_active",
        "is_deleted",
        "created_date",
        "updated_date",
        "area__name",
    )
    ordering = ("is_deleted", "is_active")


admin.site.register(User, UserAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserAd, UserAdAdmin)
# admin.site.register(SavedAd)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Banner, BannerAdmin)
