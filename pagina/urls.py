from django.urls import path, include
from pagina import views as WeViews
from .models import *

urlpatterns = [
    path('',WeViews.HomePage,name='home'),
    path('events/',WeViews.EventIndexView,name='events_index'),
    path('events/<int:id>',WeViews.EventShowView,name='show_event'),
    path('create_event/', WeViews.CreateEventView, name='create_event'),
    path('delete_event/<int:id>/', WeViews.DeleteEventView, name='delete_event'),
    path('profile/', WeViews.ShowProfile, name='profile'),
    path('delete_user/<int:id>/', WeViews.DeleteUser, name='delete_user'),
    path('support/',WeViews.Support, name='support'),
]