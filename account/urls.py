from django.urls import path
from .views import *


urlpatterns = [
path('login/', login_view, name="urllogin"),
path('logout/', logout_view, name="urllogout"),
path('signup/', signup_view, name="urlsignup"),
]