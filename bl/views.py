from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
	context={
		'posts': Post.objects.all()
	}
	return render(request,'bl/home.html',context)

def about(request):
	return render(request,'bl/about.html',{'title':'About Page'})
# Create your views here.
