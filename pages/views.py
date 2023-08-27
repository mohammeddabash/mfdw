# pages\views.py
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.shortcuts import HttpResponse
import datetime
from . models import page
import math
def home(request):
    context={
        'page_list': page.objects.all(),
    }
    return render(request,'pages/home.html',context)


def index(request,pagename):
    pagename='/'+pagename
    pg=get_object_or_404(page,permalink=pagename)
   # bk=book.objects.all()
    #bk2=book.objects.filter(bk.pub_date.month>=timezone.now().month-datetime.timedelta(month=1))
   # bk3=bk2.count()
    context = {
    'title': pg.title,
    'content': pg.bodytext,
    'last_updated': pg.update_data,
    'page_list':page.objects.all(),

    }
    #assert False
    return render(request,'pages/page.html',context)

def about(request):
    context = {
        'page_list': page.objects.all(),
    }
    return render(request,'pages/about.html',context)

def our_services(request):
    context = {
        'page_list': page.objects.all(),
    }
    return render(request,'pages/our_services.html',context)

def contact_us(request):
    context = {
        'page_list': page.objects.all(),
    }
    return render(request,'pages/contact_us.html',context)