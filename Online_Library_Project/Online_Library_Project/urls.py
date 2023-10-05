from django.contrib import admin
from django.urls import include, path  # Import include

from home.views import APISchemaView  # Import your schema view
from add_chapters.views import APISchemaView
from book_logic.views import APISchemaView
from books.views import APISchemaView
from books_list.views import APISchemaView
from cart.views import APISchemaView
from dashboard.views import APISchemaView
from employee_dashboard.views import APISchemaView
from login_app.views import APISchemaView
from users.views import APISchemaView

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
    path("api/schema/", APISchemaView.as_view(), name="api-schema"),
]
