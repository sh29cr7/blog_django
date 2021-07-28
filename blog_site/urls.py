from . import views
from django.urls import path

urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('simpleupload/',views.model_form_upload,name='upload'),
    path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
    
]