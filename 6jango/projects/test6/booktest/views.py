#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from models import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from task import *

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

#自定义编辑器
def htmlEditor(request):
    return render(request, 'booktest/htmlEditor.html')
def htmlEditorHandle(request):
    html=request.POST['hcontent']
    # test1=Test1.objects.get(pk=1)
    # test1.content=html
    # test1.save()
    test1=Test1()
    test1.content=html
    test1.save()
    context={'content':html}
    return render(request,'booktest/htmlShow.html',context)

#缓存
#@cache_page(60*10)
def cache1(request):
    # return HttpResponse('hello1')
    # return HttpResponse('hello2')
    # cache.set('key1','value1',600)
    # print(cache.get('key1'))
    # return render(request,'booktest/cache1.html')
    cache.clear()
    return HttpResponse('ok')

#全文检索+中文分词
def mysearch(request):
    return render(request,'booktest/mysearch.html')

#celery异步
def celeryTest(request):
    # show()
    show.delay()
    return HttpResponse('ok')

