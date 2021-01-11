
from django.conf.urls import url
from hospital.app.client.views import ShiftRegisterationView, ShiftListView


urlpatterns = [
    url(r'^shiftcreate',ShiftRegisterationView.as_view()),
    url(r'^shiftview',ShiftListView.as_view()),
    ]
