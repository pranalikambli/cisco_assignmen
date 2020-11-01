from django.urls import include, path
from . import views

urlpatterns = [
  path('get', views.GetRoutersAPI.as_view()),
  path('create', views.CreateRounterAPI.as_view()),
  path('update/<str:loopback>', views.UpdateRouterAPI.as_view()),
  path('delete/<str:loopback>', views.DeleteRouterAPI.as_view()),
  path('getsapid/<str:sapid>', views.GetRoutersSapIdAPI.as_view()),
  path('getiprange/<str:ip_range>', views.GetRoutersIpRangeAPI.as_view())
]