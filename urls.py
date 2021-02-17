"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import include  #include() fn ko use kiye haii isly import kiye haii
from testapp import views as testapp_views
from exam import views as exam_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from ImageUploader import views
from Hero import views
from OMAR import views
from Quiz import views
from Covid import views
from PAYMENT import views
from Download import views
urlpatterns = [
    url('testapp',include('testapp.urls')),
    url('exam',include('exam.urls')),
    url('Enroll',include('Enroll.urls')),
    url('BRMapp',include('BRMapp.urls')),
    url('Test',include('Test.urls')),
    url('Geeks',include('Geeks.urls')),
    url('Store',include('Store.urls')),
    url('Youtube',include('Youtube.urls')),
    #path('home/', views.homepage, name='home'),
    #path('save/', views.saveData, name='save'),
    #path('delete/', views.deleteData, name='delete'),
    #path('edit/', views.editData, name='edit'),
    #path('result/', exam_views.showResult),
    #path('about/', testapp_views.about),
    #path('contact/', testapp_views.showContact),
    #url('^$',testapp_views.greeting),
    #---------------------------------------------------AJAX----------------------------------
    #path('home/',views.ajaxhome),
    #path('sign/',views.signpage),
    #path('sign_up/',views.user_signup),
    #path('add-book/',views.addBook),
    #path('add/',views.Addbook),
    #path('show/',views.showBook),
    #path('checkEmail/',views.check_email),

    #--------------------------------------------------------
    #path('home/',views.homepage),
    url('Quiz',include('Quiz.urls')),
    url('Covid',include('Covid.urls')),
    url('Download',include('Download.urls')),
    path('admin/', admin.site.urls),
    url('PAYMENT',include('PAYMENT.urls')),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
