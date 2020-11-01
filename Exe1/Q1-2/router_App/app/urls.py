from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.RouterInfoList.as_view(), name='router_list'),
    path('create', views.RouterAdd.as_view(), name='create'),
    path('update/<int:pk>', views.RouterInfoUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='delete'),
]
