from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("posts/", include("posts.urls")),
    path("authentication/", include("account.urls")),
    path("ckeditor", include("ckeditor_uploader.urls")),
    path("contact/", include("contact.urls"))

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
