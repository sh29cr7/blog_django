from . import views
from django.urls import path
from blog_site.views import model_form_upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('simpleupload/',model_form_upload,name='upload'),
    path('displayuploaded/',model_form_upload,name='disp'),
    path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)