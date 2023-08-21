from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .yasg import urlpatterns as doc_urls


urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Third-party apps
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.authtoken")),
    path("api/auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # Local apps
    path("api/shop/", include("shop.urls")),
    path("api/cart/", include("cart.urls")),
    path("api/order/", include("order.urls")),
    path("api/profile/", include("customer.urls")),
    path("api/mailing/", include("mailing.urls")),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
