from django.contrib import admin
from django.urls import path
from BLOG_POSTS import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [

        path('register/',views.create,name="register"),
        path('success/',views.success,name="success"),
        path('home/',views.home,name="home"),
        path('create_blog/',views.create_blog,name='create_blog'),
        path('show/',views.show,name='show'),
        path('delete/<int:id>',views.destroy),
        path('edit/<int:id>',views.edit,name='edit'),
        path('update/<int:id>', views.update,name='update')

    ]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
