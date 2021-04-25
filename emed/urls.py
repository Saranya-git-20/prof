from django.conf.urls import url
from emed import views
from django.urls import path
from django.conf.urls import url
from .views import (categoryListView)




app_name = 'emed'

urlpatterns=[
    path('x', categoryListView.as_view(),name='product_view'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    
]