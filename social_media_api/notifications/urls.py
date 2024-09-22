from django.urls import path
from .views import NotificationListView
from django.urls import path, include
urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),  # Include notification URLs

]

