from django.contrib import admin
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.main_page, name='name_page'),
]
