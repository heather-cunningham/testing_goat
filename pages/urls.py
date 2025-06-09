from django.urls import path
from pages.views import homepage


app_name = "pages"


urlpatterns = [
    path("", homepage, name="homepage"),
]