from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:producto_id>', views.ver_producto, name='ver_producto'),
    path('edit/<int:producto_id>/', views.edit_producto, name='edit'),
    path('add', views.add, name='add'),
    path('delete/<int:producto_id>/', views.delete, name='delete'),
]