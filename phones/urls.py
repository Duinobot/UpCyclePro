from django.urls import path


from .views import *

urlpatterns = [
    path('', PhoneListView.as_view(), name='PhoneListView'),
    path('create/', PhoneCreateView.as_view(), name='PhoneCreateView'),
]