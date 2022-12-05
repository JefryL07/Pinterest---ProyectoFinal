from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = "main"

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', login_required(views.IndexView.as_view()), name="home"),
	path('contact/', views.ContactView.as_view(), name="contacto"),
	path('pubAddInfo/', login_required(views.pubAddAnfo.as_view()), name="addinfo"),
	path('Animales/', views.AnimalView.as_view(), name="animal"),
	path('Paisajes/', views.PaisaView.as_view(), name="Paisajes"),
	path('Outfits/', views.OutfitView.as_view(), name="Outfits"),
	path('Tatto/', views.TattoView.as_view(), name="Tatuajes"),
	path('Maquillaje/', views.MaquiView.as_view(), name="Maquillaje"),

	]