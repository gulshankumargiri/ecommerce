"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from mainapp import views

urlpatterns = [
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('home/',views.homepage, name="homepage"),
    path('cart/',views.addcart, name="addcart"),
    path('',views.homepage, name="homepage"),
    path('about/',views.about, name="about"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addpost/',views.addpost, name="addpost"),
    path('updatepost/<int:id>',views.updatepost, name="updatepost"),
    path('deletepost/<int:id>',views.deletepost, name="deletepost"),
    path('contact/',views.contact, name="contact"),
    path('sign_up/',views.user_signup, name="sign_up"),
    path('login/',views.user_login, name="user_login"),
    path('user_logout/',views.user_logout, name="user_logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),  
    # path(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    # path(r'^cart/', views.mycart, name='cart'),

]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


