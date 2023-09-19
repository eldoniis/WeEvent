from django.urls import path, include
from .views import *
from .models import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('events/',EventIndexView.as_view(),name='events_index'),
    path('events/<int:id>',EventShowView.as_view(),name='show_event'),
    path('create_event/', CreateEventView.as_view(), name='create_event'),
    path('delete_event/<int:id>/', DeleteEventView.as_view(), name='delete_event'),
]