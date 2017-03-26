from django.conf.urls import url
from . import views

urlpatterns = [
    # ADMIN PRIVILEGES
    # ADMIN PRIVILEGES
    url(r'^$', views.ProductList.as_view()),
    url(r'^add/$', views.AddProduct.as_view()),
]
