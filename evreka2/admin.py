from typing import Collection
from django.contrib import admin
from .models import Bin, Operation, Collection

# Register your models here.
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(Collection)