from django.urls import path
from longclaw.longclawshipping import api
from longclaw.settings import API_URL_PREFIX

address_list = api.AddressViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
address_detail = api.AddressViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path(API_URL_PREFIX + 'addresses/', address_list, name='longclaw_address_list'),

    path(API_URL_PREFIX + 'addresses/<int:pk>/', address_list, name='longclaw_address_detail'),

    path(API_URL_PREFIX + 'shipping/cost/', api.shipping_cost, name='longclaw_shipping_cost'),

    path(API_URL_PREFIX + 'shipping/countries/', api.shipping_countries, name='longclaw_shipping_countries'),

    path(API_URL_PREFIX + 'shipping/countries/<str:country>/', api.shipping_options, name='longclaw_shipping_options'),
]
