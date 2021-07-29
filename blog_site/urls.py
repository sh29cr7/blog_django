from . import views
from django.urls import path
from blog_site.views import model_form_upload

urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('simpleupload/',model_form_upload,name='upload'),
    path('displayuploaded/',file_upload_disp,name='disp')
    path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
    
]