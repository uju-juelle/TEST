from django.urls import path
from .views import *

urlpatterns = [
    path("", news_homepage.as_view(), name="home"),
    path("<slug:slug>/", news_detailpage.as_view(), name="detail"),
]

