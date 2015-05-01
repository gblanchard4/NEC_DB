from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /patients/
    url(r'^$', views.index, name='index'),
    # ex: /patients/22/
    url(r'^(?P<patientid>[0-9]+)/$', views.patient_detail, name='detail'),
    # ex: /patient/22/stool/1
    url(r'^(?P<patientid>[0-9]+)/stool/$', views.stool_single, name='stool')
]