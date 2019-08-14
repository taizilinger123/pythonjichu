from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))


#manage.py(os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test3.settings"))->settings.py(ROOT_URLCONF = 'test3.urls')
#->test3/urls.py(url(r'^booktest/', include('booktest.urls')))->booktest/urls.py(url(r'^$',views.index),)
#->booktest/views.py(def index(request):)
#(h5) sige@sige1:~/Desktop/projects$ django-admin startproject test3
#(h5) sige@sige1:~/Desktop/projects$ cd  test3
#(h5) sige@sige1:~/Desktop/projects/test3$ python manage.py startapp booktest
#(h5) sige@sige1:~/Desktop/projects/test3$ python manage.py runserver
#http://127.0.0.1:8000/booktest/
#http://127.0.0.1:8000/booktest/123
#http://127.0.0.1:8000/booktest/2016/12/27/