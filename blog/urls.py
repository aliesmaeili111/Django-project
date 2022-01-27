from turtle import pos
from .  import views
from django.urls import path

urlpatterns = [
    path('',views.post_list,name = 'post_list'),
    path('<str:tag_slug>/',views.post_list,name = 'post_list_tag'),
    path('contact-us/',views.contact_us,name = 'contact_us'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',views.post_detail,name = 'post_detail'),
]