from django.urls import path
from . import views

app_name = "posts"


urlpatterns = [
    path("<int:id>", views.post_view, name = "post"),
    path("random/", views.random_post, name = "randomPost")
]
