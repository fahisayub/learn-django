from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path('fahiz',views.fahiz,name="fahiz"),
    path('<str:name>',views.greetuser,name='greetuser'),
    # path('<str:name>',views.greet,name='greet'),
]