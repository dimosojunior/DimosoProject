from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from DimosoApp.forms import *
from hitcount.views import HitCountDetailView
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
	

def Documents(request, mydocumentstype_slug=None):
	mydocumentstype = None
	categories = MyDocumentsType.objects.all()
	files = MyDocuments.objects.all().order_by('-id')

	

	#SET PAGINATION kWA AJILI YA NOTES
	paginator = Paginator(files, 6)
	page = request.GET.get('page')
	try:
	  files=paginator.page(page)
	except PageNotAnInteger:
	  files = paginator.page(1)
	except EmptyPage:
	  files=paginator.page(pagenator.num_pages)
	form = MyDocumentsForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    #MWISHO WA PAGINATION
    #searching button codes LKN HAITUMIKI TENA HAPA NIMETIMIA ILE YA KWENYE SEARCH_PDF
	if request.method == 'POST':
	    files = MyDocuments.objects.filter( name__icontains=form['name'].value())
	#hizi codes ni kwa ajili ya kudisplay category 
	if mydocumentstype_slug:
		files = MyDocuments.objects.all()

		mydocumentstype = get_object_or_404(MyDocumentsType,slug=mydocumentstype_slug)
		files= files.filter(mydocumentstype=mydocumentstype)

		#SET PAGINATION KWA AJILI YA CATEGORY
		paginator = Paginator(files, 6)
		page = request.GET.get('page')
		try:
			files=paginator.page(page)
		except PageNotAnInteger:
			files = paginator.page(1)
		except EmptyPage:
			files=paginator.page(pagenator.num_pages)
#ZINAISHIA HAPA




	context = {
		"form":form,
		"categories":categories, 
		"mydocumentstype":mydocumentstype,


		"files":files,
		"page":page

	}

	return render(request, 'files/MyDocuments.html',context)

def search_mydocuments(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=MyDocuments.objects.filter(Q(name__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'files/search_mydocuments.html',context)

def search_mydocument(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    files = MyDocuments.objects.filter(search)
    mylist= []
    mylist += [x.name for x in files]
    return JsonResponse(mylist, safe=False)
#HII NI KWA AJILI YA KUAPLOAD NOTES KWA KUTUMIA FORM  
def upload_mydocuments(request):
	categories = MyDocumentsType.objects.all()
	if request.method == 'POST':
		data = request.POST
		pdf = request.FILES.get('pdf')
		cover = request.FILES.get('cover')
		if data['mydocumentstype'] != 'none':
			mydocumentstype = MyDocumentsType.objects.get(id=data['mydocumentstype'])
		#elif data['filecourse_new'] != '':
			#filecourse, created = FileCourse.objects.get_or_create(name=data['filecourse_new'])
		else:
			mydocumentstype = None
		files = MyDocuments.objects.create(
				mydocumentstype=mydocumentstype,
				name = data['name'],
				owner = data['owner'],
				year = data['year'],
				cover=cover,
				pdf=pdf,

			)
		messages.success(request, "File uploaded successful")
		return redirect('Documents')



	context={
		"categories":categories,
		
		

	}
	

	return render(request, 'files/upload_mydocuments.html',context)