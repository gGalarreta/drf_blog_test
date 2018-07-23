from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/blog/', include('blog.api.urls', namespace='api-blog')),
]
