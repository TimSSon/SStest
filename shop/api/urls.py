from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('items', ItemListView.as_view()),
    path('profile/update/<int:pk>/', ProfileEdit.as_view()),
    

]
