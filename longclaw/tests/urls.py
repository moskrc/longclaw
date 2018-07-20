# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import include, path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from longclaw import urls as longclaw_urls
from longclaw.contrib.productrequests import urls as request_urls

urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('', include(longclaw_urls)),
    path('', include(request_urls)),
    path('', include(wagtail_urls)),

]
