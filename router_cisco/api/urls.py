from django.urls import path,re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('router/create', views.RouterCreateApi.as_view(), name='router_create'),
    path('',views.RouterApi.as_view(),name='router_list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/<str:loopback>/',views.RouterDetails.as_view(),name='edit'),
    path('api/<int:id>/delete',views.RouterDetails.as_view(),name='delete')

]