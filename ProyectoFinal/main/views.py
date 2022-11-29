from django.shortcuts import render
from django.views import generic

from .models import (
		UserProfile,
        Publicaciones
)
# Create your views here.
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		publicaciones = Publicaciones.objects.filter(is_active=True)

		
		context["publicaciones"] = publicaciones

		return context