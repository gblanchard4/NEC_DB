from django.conf.urls import patterns, include, url
from django.contrib import admin

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'nectar.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^patients/', include('patients.urls'))
# )
urlpatterns = [
    url(r'^patient/', include('patients.urls')),
    url(r'^admin/', include(admin.site.urls))
]