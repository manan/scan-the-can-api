from django.conf.urls import url
from . import views

urlpatterns = [
    # ADMIN PRIVILEGES
    url(r'^$', views.ReceiptList.as_view()),
    url(r'^add/$', views.BuildReceipt.as_view()),
]
