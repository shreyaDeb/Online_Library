from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include your app-specific URLs here
    path('books/', include('books_list.urls')),
    path('book_logic/', include('book_logic.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),  # Include users app URLs
    path('login_app/', include('login_app.urls')),  # Include login_app app URLs
    path('dashboard/', include('dashboard.urls')),  # Include dashboard app URLs
    path('employee_dashboard/', include('employee_dashboard.urls')),  # Include employee_dashboard app URLs
    path('add_chapters/', include('add_chapters.urls')),  # Include add_chapters app URLs
]
