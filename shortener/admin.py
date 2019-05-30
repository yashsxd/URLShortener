from django.contrib import admin
from shortener.models import Urls

# Registering URLs in admin menu
admin.site.register(Urls)