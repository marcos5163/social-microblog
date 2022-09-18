from django.urls import path
from blog.views import UserAccountViewSet

urlpatterns = [
    path("authenticate-user/", UserAccountViewSet.as_view({"post": "authenticate"})),
    path("create-user/", UserAccountViewSet.as_view({"post": "create_user", "patch":"change_password"}))
]
