from django.urls import path
from ecommerceapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name ="index"),
    path('contact/', views.contact , name ="contact"),
    path('about/', views.about , name ="about"),
    path('profile/', views.profile, name ="profile"),
    path('checkout/', views.checkout , name ="checkout"),
    path('handlerequest/', views.handlerequest , name ="HandleRequest"),
]



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)