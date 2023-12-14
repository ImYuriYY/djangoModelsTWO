from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('create/', createNews, name='create'),
    path('change/<int:id>', change, name='change'),
    path('delete/<int:id>', delete, name='delete')
]