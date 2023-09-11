from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('person.urls')),
    path('', TemplateView.as_view(template_name='index.html'),
         name='home'),  # Handle the root URL
]
