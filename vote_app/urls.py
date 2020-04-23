from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('vote/<int:vote_id>',views.vote,name='vote'),
    path('result/<int:vote_id>',views.result,name='result'),
    path('create/',views.create,name='create'),

]
