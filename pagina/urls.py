from django.urls import path, include
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('events/',EventIndexView.as_view(),name='events_index'),
    path('events/<int:id>',EventShowView.as_view(),name='show_event'),
]