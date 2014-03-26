from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

admin.autodiscover()
# router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
# router.register(r'aluno', views.ClienteViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^rest/', include(router.urls)),
    url(r'^rest/user-create', views.UserCreate.as_view()),
    url(r'^rest/user-list', views.UserList.as_view()),

    url(r'^', 'app.views.index'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
