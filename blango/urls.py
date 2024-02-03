from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django_registration.backends.activation.views import RegistrationView
from django.contrib.auth import views as auth_views
from blango_auth.forms import BlangoRegistrationForm

import blog.views
import debug_toolbar
import blango_auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
     path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]