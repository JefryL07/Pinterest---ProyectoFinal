from django import forms
from .models import Publicaciones, ContactProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class ReviewForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,			# Campo para el author de la review del anime
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True,			# Campo para el Nombre del anime
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True,	# Campo para la descripcion
		widget=forms.TextInput(attrs={
			'placeholder': '*Description info..',
			}))
	body = forms.CharField(max_length=500, required=True,			# Campo para el contenido de la review
		widget=forms.Textarea(attrs={
			'placeholder': '*Body info..',
			}))
	image = forms.ImageField()										# Campo para subir una imagen del anime

	class Meta:
		model = Publicaciones
		fields = ['author', 'name', 'description', 'body', 'image']


# Formulario para ingresar un nuevo blog de anime o manga
class PublicacionForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,  
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Description info..',
			}))
	body = forms.CharField(max_length=500, required=True,
		widget=forms.Textarea(attrs={
			'placeholder': '*Body info..',
			}))
	image = forms.ImageField()

	class Meta:
		model = Publicaciones
		fields = ['author', 'name', 'description', 'body', 'image']


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)