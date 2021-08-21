from django.urls import path
from .views import HomePagesView

urlpatterns = [
    path('', HomePagesView.as_view(), name = 'home'),
]