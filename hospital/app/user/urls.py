from django.conf.urls import url
from hospital.app.user.views import UserRegistrationView
from hospital.app.user.views import UserLoginView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    ]
