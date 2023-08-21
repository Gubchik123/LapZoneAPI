from django.urls import path

from . import views


urlpatterns = [
    path("carousel-images/", views.CarouselImageListAPIView.as_view()),
    path(
        "recently-added-products/",
        views.RecentlyAddedProductListAPIView.as_view(),
    ),
    path("brands/", views.BrandListAPIView.as_view()),
    path("categories/", views.CategoryListAPIView.as_view()),
    path("products/", views.ProductListAPIView.as_view()),
    path("search/", views.ProductSearchListAPIView.as_view()),
    path("brand/<slug:slug>/", views.ProductByBrandListAPIView.as_view()),
    path(
        "category/<slug:slug>/", views.ProductByCategoryListAPIView.as_view()
    ),
    path("product/<slug:slug>/", views.ProductRetrieveAPIView.as_view()),
    path("review/", views.ProductReviewCreateAPIView.as_view()),
    path("like/", views.ProductLikeCreateAPIView.as_view()),
    path("like/<int:pk>/", views.ProductLikeDestroyAPIView.as_view()),
]
