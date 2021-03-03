from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from accounts.models import AuthToken, Profile
from webapp.models import Item
from .serializer import RegisterSerializer, ItemSerializer, ProfileSerializer, UpdateUserSerializer
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        user = request.data
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = get_user_model().objects.get(email=user_data['email'])
            token = self.create_token(user)
            self.send_email(user, token)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_token(self, user):
        return AuthToken.objects.create(user=user)

    def send_email(self, user, token):
        if user.email:
            subject = 'Вы создали учётную запись на сайте "Localhost"'
            link = settings.BASE_HOST + \
                reverse('accounts:activate', kwargs={'token': token.token})
            message = f'''Здравствуйте, {user.username}!
Вы создали учётную запись на сайте "Localhostг"
Активируйте её, перейдя по ссылке {link}.
Если вы считаете, что это ошибка, просто игнорируйте это письмо.'''
            html_message = f'''Здравствуйте, {user.username}!
Вы создали учётную запись на сайте "Localhost"
Активируйте её, перейдя по ссылке <a href="{link}">{link}</a>.
Если вы считаете, что это ошибка, просто игнорируйте это письмо.'''
            try:
                user.email_user(subject, message, html_message=html_message)
            except Exception as e:
                print(e)


class ItemListView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class UserEdit(RetrieveUpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = get_user_model().objects.all()
    # permission_classes = (IsOwnerReadOnly,)
