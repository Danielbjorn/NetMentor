from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def index(request): 
	return render(request, 'index.html', {} )

def signup(request): 
	return render(request, 'signup.html',  {})
    