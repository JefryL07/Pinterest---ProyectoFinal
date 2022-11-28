from django import forms
from .models import Publicaciones

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