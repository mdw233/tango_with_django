from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says Hey Now! <a href ='about'>About</a>")

def about(request):
	return HttpResponse("Rango says: This is the about page! <a href ='/rango'>Home</a>")
