from django.urls import path
from .views import AlbumView, MusicianView

urlpatterns = [
    # http://127.0.0.1:8000/api/albums/
    path('', AlbumView.as_view({ 
        'get': 'list',
        'post': 'create'
    })),
    # http://127.0.0.1:8000/api/albums/id/
    path('<int:id>/', AlbumView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
    })),
    # http://127.0.0.1:8000/api/albums/musicians/
    path('musicians/', MusicianView.as_view({ 
        'get': 'list',
    })),
]
