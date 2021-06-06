from django.contrib import admin
from django.urls import path
from users import views as user_views

#   Static files config
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.login, name='login'),
    path('new/', user_views.signup, name='signup')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
