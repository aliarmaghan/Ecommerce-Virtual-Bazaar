from django.urls import path
from ecommerceapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name ="index"),
    path('contact', views.contact , name ="contact"),
    path('about', views.about , name ="about")
]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)