from django.conf.urls import url
from . import views

urlpatterns = [
    # ADMIN PRIVILEGES
    url(r'^$', views.ReceiptList.as_view()),
    url(r'^add/$', views.AddReceipt.as_view()),
    url(r'^add/username=(?P<username>.+)/company=(?P<comp>.+)/$', views.add_products),
    url(r'^addproducts/receipt=(?P<rec_id>.+)/barcodes=(?P<barcodes>.+)/$', views.add_products),
]
