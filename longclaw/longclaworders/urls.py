from django.urls import path
from longclaw.longclaworders import api

from longclaw.settings import API_URL_PREFIX


API_URL_PREFIX = API_URL_PREFIX.lstrip('/')

orders = api.OrderViewSet.as_view({
    'get': 'retrieve'
})

fulfill_order = api.OrderViewSet.as_view({
    'post': 'fulfill_order'
})

refund_order = api.OrderViewSet.as_view({
    'post': 'refund_order'
})

PREFIX = '{}order/'.format(API_URL_PREFIX)
urlpatterns = [
    path(
        PREFIX + '<int:pk>/',
        orders,
        name='longclaw_orders'
    ),

    path(
        PREFIX + '<int:pk>/fulfill/',
        fulfill_order,
        name='longclaw_fulfill_order'
    ),

    path(
        PREFIX + '<int:pk>/refund/',
        refund_order,
        name='longclaw_refund_order'
    )
]
