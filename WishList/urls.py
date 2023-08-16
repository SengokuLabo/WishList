
from django.urls import path
from . import views

urlpatterns = [
    path("api/create_user/", views.create_user_api, name="create_user_api"),
    path("api/get_token/", views.get_token_api, name="get_token_api"),
    # path('admin/', admin.site.urls),
]
