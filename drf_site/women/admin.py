from django.contrib import admin
from .models import Women, Category


# Register our models so that they are available at the admin endpoint
admin.site.register(Women)
admin.site.register(Category)
