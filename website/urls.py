from django.conf.urls import url
from django.contrib import admin
from Blogs import views

urlpatterns = [
    url(r"^$", views.homepage),
    url(r"^index.html", views.homepage),
    url(r"^blog.html", views.blog),
    url(r"^about-me.html", views.aboutMe),
    url(r'^admin/', admin.site.urls),
]
