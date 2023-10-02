from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .serializers import LampSerializer
from .models import Lamp

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


@login_required
def api_token_list(request):
    user = request.user
    tokens = Token.objects.filter(user=user)

    context = {
        'tokens': tokens
    }
    return render(request, 'devices/api_token_list.html', context)


class TokenHasReadWriteScope(BasePermission):
    message = 'Token has not the required scope.'

    def has_permission(self, request, view):
        # Stellen Sie sicher, dass der Benutzer authentifiziert ist
        if not request.user or not request.user.is_authenticated:
            return False

        # Stellen Sie sicher, dass der Benutzer ein gültiges API-Token hat
        return TokenAuthentication().authenticate(request)


class LampList(generics.ListCreateAPIView):
    serializer_class = LampSerializer
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

    def get_queryset(self):
        # Filtere die Lampen nach dem angemeldeten Benutzer
        return Lamp.objects.filter(user=self.request.user)


class LampDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lamp.objects.all()
    serializer_class = LampSerializer
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]


@login_required
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_api_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return redirect('devices:api_token_list')
