from django.contrib import admin
from django.urls import path
from vegetable.views import receipes
from django.conf import settings
from django.conf.urls.static import static
from vegetable.views import delete_receipe
from vegetable.views import home
from vegetable.views import update_receipe


urlpatterns = [
    path('',home, name='home'),  # Home page
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name='receipes'),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update_receipe/<int:id>/',update_receipe, name='update_receipe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)