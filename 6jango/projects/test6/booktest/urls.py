from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
]