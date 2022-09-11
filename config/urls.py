
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from music.api import songRouter
api=NinjaAPI()
api.add_router('/', songRouter)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('chaining/', include('smart_selects.urls')),
]
