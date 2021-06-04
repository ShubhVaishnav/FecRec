from django.conf.urls import url
from . import views
from .views import test_image_view, display_test_image
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy


app_name = 'persons'

urlpatterns = [

    # for /persons/
    url(r'^$', views.page1 , name='page1'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<character_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^image_upload/$', views.test_image_view, name='image_upload'),
    url(r'^output/$', views.output, name='output'),
    url(r'^mainCode/$', views.mainCode, name='mainCode'),
    url(r'^countCode/$', views.countCode, name='countCode'),

]

# successmsg = reverse_lazy('seccessmsg')

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

