from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student_login/', views.student_login, name='student_login'),
    path('detail/', views.detail, name='detail'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('final_submit/', views.final_submit, name='final_submit'),
    path('faculty_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('f_dashboard/', views.f_dashboard, name='f_dashboard'),
    path('btn_save/', views.btn_save, name='btn_save'),
    path('update/', views.update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)