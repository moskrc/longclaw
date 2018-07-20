from django.urls import include, path
from longclaw.longclawbasket import urls as basket_urls
from longclaw.longclawcheckout import urls as checkout_urls
from longclaw.longclawshipping import urls as shipping_urls
from longclaw.longclaworders import urls as order_urls

urlpatterns = [
    path('', include(basket_urls)),
    path('', include(checkout_urls)),
    path('', include(shipping_urls)),
    path('', include(order_urls)),
]
