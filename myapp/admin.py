from django.contrib import admin
from .models import Cpu,Ram, Display, HardDisk,Sound

# Register your models here.
admin.site.register(Cpu)
admin.site.register(Ram)
admin.site.register(Display)
admin.site.register(HardDisk)
admin.site.register(Sound)