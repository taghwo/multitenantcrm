from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from django.contrib.auth import authenticate, login, logout
from .serializer import (AuthenticationSerializer,
                         UserSerializer,
                         RegistrationSerializer,
                         RefreshTokenSerializer
                         )
from django.contrib.auth.models import User
from account.models import Account
from tenant.serializer import TenantSerializer
from .tasks import new_user_job

class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = AuthenticationSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=request.POST['email'], password=request.POST['password'])


        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)

            get_user = UserSerializer(Account.objects.filter(email=user.email).first())

            context = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user': get_user.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        serialized_user = RegistrationSerializer(data=request.data, context={'request': request})

        serialize_tenant = TenantSerializer(data=request.data)

        if not serialized_user.is_valid(raise_exception=True):
            return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

        if not serialize_tenant.is_valid(raise_exception=True):
            return Response(serialize_tenant.errors, status=status.HTTP_400_BAD_REQUEST)
        else:

            user = serialized_user.save()

            tenant = serialize_tenant.save()

            user.tenant = tenant

            user.save()

            refresh = RefreshToken.for_user(user)

            context = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user': serialized_user.data
                }

            new_user_job.delay(user=serialized_user.data)

        return Response(context, status=status.HTTP_200_OK)


class AuthUser(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.id)

        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RefreshTokenSerializer

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
