from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.http import JsonResponse


def api_view(request):
    # API LOGIC
    return JsonResponse({"message": "API response"})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
