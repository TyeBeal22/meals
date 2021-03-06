
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('meals/' , include('meals.urls' , namespace='meals')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('contact/' , include('contact.urls' , namespace='contact')),
    path('about-us/' , include('aboutus.urls' , namespace='aboutus')),
    path('reserve_table/' , include('reservation.urls' , namespace='reservation')),
    path('' , include('home.urls' , namespace='home')),
    path('accounts/', include('accounts.urls')),   
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Resturant AdminPanel"
admin.site.site_title = "Resturant App Admin "
admin.site.site_index_title = "Welcome To Resturant Admin Panel"