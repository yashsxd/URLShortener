from django.urls import path, re_path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='home'),

    # Creating Short Urls
    path('short',views.short,name='short'),

    # Redirecting to Original Urls
    re_path(r'(?P<shortUrl>\w+)', views.redirector, name='redirect'),
]