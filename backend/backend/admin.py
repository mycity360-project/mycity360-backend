from django.contrib import admin

from .models.user import User
from .models.area import Area
from .models.state import State
from .models.location import Location
from .models.system_config import SystemConfig
from .models.category import Category
from .models.user_ad import UserAd
from .models.saved_ad import SavedAd
from .models.service import Service

admin.site.register(User)
admin.site.register(Area)
admin.site.register(State)
admin.site.register(Location)
admin.site.register(SystemConfig)
admin.site.register(Category)
admin.site.register(UserAd)
admin.site.register(SavedAd)
admin.site.register(Service)
