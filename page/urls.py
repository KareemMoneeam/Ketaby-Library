from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name='Index.html'),
path('login/',views.login_view, name='login.html'),
path('Collection/',views.collection, name='Collection.html'),
path('Information/',views.information, name='Information.html'),
path('profile/',views.profile, name='profile.html'),
path('index/',views.index, name='index.html'),
path('signup/',views.signup, name='signup.html'),
path('logout/',views.logout_view, name="logout"),

]