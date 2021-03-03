from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView, ItemListView, UserEdit

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('items/', ItemListView.as_view()),
    path('user/update/<int:pk>/', UserEdit.as_view()),
    

]
