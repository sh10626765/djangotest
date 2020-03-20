from django.urls import path
from . import views


urlpatterns =[
    path('',views.index, name='index'),
    path('upload/', views.upload_data, name='upload_data'),
    path('show/', views.show_data, name='show_data'),
    path('update/', views.update_data, name='update_data'),
    path('base/', views.index, name='index'),
]