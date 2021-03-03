from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView, ItemListView, ProfileEdit

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('items/', ItemListView.as_view()),
    path('profile/update/<int:pk>/', ProfileEdit.as_view()),
    

]
