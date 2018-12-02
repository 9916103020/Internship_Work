from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    url(r'choice/$',views.choice),
    url(r'profile/$',views.profile,name='profile'),
]
