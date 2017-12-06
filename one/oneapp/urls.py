from django.conf.urls import url,include
from oneapp import views

# Template URLS !

app_name = 'oneapp'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='login')

]
