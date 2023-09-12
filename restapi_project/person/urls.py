from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView, PersonByNameView

urlpatterns = [
    path('', PersonListCreateView.as_view(), name='person-list-create'),
    path('<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(),
         name='person-retrieve-update-destroy'),
    path('<str:name>/', PersonByNameView.as_view(), name='person-by-name'),
]
