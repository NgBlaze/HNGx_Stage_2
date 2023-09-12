from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('person.urls')),

]
