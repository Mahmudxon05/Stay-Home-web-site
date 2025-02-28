from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name = 'index-url'),
    path('send-message/', send_message_view, name='send-message-url' ),
]