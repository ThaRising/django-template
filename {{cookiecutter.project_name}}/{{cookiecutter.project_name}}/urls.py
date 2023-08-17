from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import UserRegistration, UserSettings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    {% if cookiecutter.use_frontend | int %}
    path("unicorn/", include("django_unicorn.urls")),
    {% endif %}
    # path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/profile/", UserSettings.as_view(), name="user-profile-edit"),
    # path("accounts/register/", UserRegistration.as_view(), name="user-register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
