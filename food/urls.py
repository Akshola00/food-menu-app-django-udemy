from django.urls import path
from . import views
# app_name = 'food' name spacnig for where there are two or more apps with same url name
urlpatterns=[
    path('', views.index.as_view(), name='index' ),
    # path('item/', views.item, name='item' ),
    path('<int:pk>', views.detail.as_view(), name='details'),

    # add view
    path('add', views.create_item.as_view(), name='create_item'),
    path('update/<int:id>/', views.update_food, name='update_food'),
    path('delete/<int:id>/', views.delete, name='delete'),
]