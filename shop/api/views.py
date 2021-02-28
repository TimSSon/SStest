from django.shortcuts import render
from .permissions import IsOwnerReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.



class AdvertUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertDetailSerializer
    queryset = Advert.objects.all()
    permission_classes = (IsOwnerReadOnly, IsAdminUser)
