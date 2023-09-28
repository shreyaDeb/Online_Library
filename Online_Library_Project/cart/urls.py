from django.urls import path

from . import views

urlpatterns = [
    path("view_cart/", views.view_cart, name="view_cart"),
    path("add_to_cart/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path(
        "remove_from_cart/<int:cart_item_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),
    # Add more URLs for cart-related views as needed
]
