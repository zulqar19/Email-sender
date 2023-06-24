from django.urls import path
# from . import views
from EmailSender.views import index

urlpatterns = [
    path('',index, name='email')
]
