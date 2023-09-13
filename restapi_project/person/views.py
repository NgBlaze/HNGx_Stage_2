# myapi/views.py
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class PersonListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.none()

    def perform_create(self, serializer):
        serializer.save()


class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'
