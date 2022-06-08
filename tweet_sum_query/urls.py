from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_sum_query_home, name='tweet_sum_query_home'),
]