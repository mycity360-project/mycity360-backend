from django.contrib import admin

from .models.user import User
from .models.area import Area
from .models.state import State
from .models.location import Location
from .models.system_config import SystemConfig

admin.site.register(User)
admin.site.register(Area)
admin.site.register(State)
admin.site.register(Location)
admin.site.register(SystemConfig)
