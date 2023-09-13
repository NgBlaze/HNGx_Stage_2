from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<str:name>/', PersonRetrieveUpdateDeleteView.as_view(),
         name='person-retrieve-update-delete'),
]
