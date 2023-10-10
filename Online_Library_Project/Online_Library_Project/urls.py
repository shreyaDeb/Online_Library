from django.contrib import admin
from django.urls import include, path  # Import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # Include your app-specific URLs here
    path("", include("books_list.urls")),
    path("", include("book_logic.urls")),
    path("", include("cart.urls")),
    path("", include("users.urls")),  # Include users app URLs
    path("", include("login_app.urls")),  # Include login_app app URLs
    path("", include("dashboard.urls")),  # Include dashboard app URLs
    path("", include("employee_dashboard.urls")),  # Include employee_dashboard app URLs
    path("", include("add_chapters.urls")),  # Include add_chapters app URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
