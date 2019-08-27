#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *

def index(request):
    return render(request,'booktest/index.html')
def pro(request):
    prolist=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    #[[1,'北京'],[2,'天津'],...]
    for item in prolist:
        list.append([item.id,item.title])#[[1,'北京']
    return JsonResponse({'data':list})
def city(request,id):
    citylist=AreaInfo.objects.filter(parea__id=id)
    list=[]
    #[{id:1,title:北京},{id:2,title:天津},...]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})