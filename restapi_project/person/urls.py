from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView, PersonByNameView

urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(),
         name='person-retrieve-update-destroy'),
    path('persons/<str:name>/', PersonByNameView.as_view(), name='person-by-name'),
]
