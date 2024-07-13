from django.urls import path # type: ignore
from django.contrib import admin
from home.views import HomeAPI,Signup,LogIn,LogOut,ChangePassword,courses

urlpatterns = [
    path('', HomeAPI, name="home-api"),
    path('signup', Signup, name="signup-api"),
    path('login', LogIn, name="login-api"),
    path('logout', LogOut, name="logout-api"),
    path('changepassword', ChangePassword, name="changepass-api"),
    path('courses',courses, name="courses"),
    
]
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # type: ignore