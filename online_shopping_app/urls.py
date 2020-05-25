from django.urls import path
from online_shopping_app import views

urlpatterns = [
    path("<category_id>/", views.CategoryProductsView.as_view(), name="category_products"),
    path("<pk>/<slug>", views.ProductsDetail.as_view(), name="single_products"),
 
 ]