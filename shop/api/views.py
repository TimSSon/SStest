from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import *
from webapp.models import *
# Create your views here.


class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ProfileEdit(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
