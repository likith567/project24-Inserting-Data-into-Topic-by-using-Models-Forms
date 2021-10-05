
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def topic_model(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('data inserted Suuceefully')
    return render(request,'topic_model.html',context={'form':form})


def webpage_model(request):
    form=WebpageForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('data inserted Suuceefully')
    return render(request,'webpage_model.html',context={'form':form})
