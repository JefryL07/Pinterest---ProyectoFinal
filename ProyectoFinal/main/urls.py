from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = "main"

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contacto"),
	path('pubAddInfo/', login_required(views.pubAddAnfo.as_view()), name="addinfo"),


	]

    