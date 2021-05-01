"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login_view ),
    url(r'^register/',views.register_view ),
    url(r'^services/',views.services_view ),
    url(r'^branch/',views.branch_view ),
    url(r'^about/',views.about_view ),
    url(r'^$',views.home_view),
    url(r'^r16cse/',views.r16cse_view ),
    url(r'^r16eee/',views.r16eee_view ),
]
