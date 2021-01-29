from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profilePage, name="profile"),
    path('editprofile/', views.editprofilePage, name="editprofile"),
    #path('profiletest/<str:pk_test>/', views . profiletest, name="profiletest"), #it works
    path('<str:username>/', views.publicprofile, name="publicprofile"), #I'm testing this, It doesn't work out
  	#path('tag/<slug:tag_slug>' views.story_list, name="story_by_tag")

    path('', views.home, name="home"),

    #path('recruiter/', views.recruiter),
    #path('talent/', views.talent),

]