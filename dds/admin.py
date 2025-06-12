from django.contrib import admin

# Register your models here.
from .models import Status
from .models import SubCategory
from .models import OperationType
from .models import MoneyOperation
from .models import Category


admin.site.register(Status)
admin.site.register(SubCategory)
admin.site.register(OperationType)
admin.site.register(MoneyOperation)
admin.site.register(Category)