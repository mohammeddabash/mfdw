from django.shortcuts import render
from .models import book
from django.views.decorators.csrf import csrf_exempt

from django.utils import timezone
from django.shortcuts import HttpResponse
import datetime
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from .forms import CreateForm
from . import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def payment_done(request,id):
    bk=get_object_or_404(book,id=id)
    context={
        'book':bk
    }
    return render(request, 'paypal/payment_done.html',context)


@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal/payment_cancelled.html')


def years_collector():
    years=set()
    books=book.objects.all()
    for b in books:
        years.add(b.pub_date.strftime('%Y'))
    return years
def year_filter(request, year):
    books_year=list()
    books=book.objects.all()
    for b in books:
        if book.year(self=b,year=year):
            books_year.append(b)

    context={
        'books_year':books_year,
        'year':year,
        'now':timezone.now().strftime('%Y')
    }
    return render(request,'books/year.html',context)

def category_year_filter(request,category,year):
    books_category_year=list()
    books=book.objects.all()
    for b in books:
        if book.year(b,year):
            books_category_year.append(b)
        if not book.category(b,category):
            books_category_year.remove(b)
    context={
        'books_category_year':books_category_year,
        'year':year,
        'now':timezone.now().strftime('%Y'),
        'category':category,
        'year_now':year>int(timezone.now().strftime('%Y'))
    }
    return render(request,'books/category_years.html',context)


#def category_year_filter(request,category,year):
 #   books_category_year=list()
  #  books=book.objects.all()
   # for b in books:
    #    if book.year(self=b,year=year) & book.category(self=b,category=category):
     #       books_category_year.append(b)
    #context={
     #   'books_category_year':books_category_year,
      #  'year':year,
       # 'category':category,
    #}
    #return render(request,'books/category_years.html',context)
from django.core.mail import send_mail
@login_required
def create(request):
    form = CreateForm(request.POST, request.FILES)
    if form.is_valid():
        instance=book(file=request.FILES['file'])
        instance.save()
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = CreateForm

    context = {
        'form':form,
    }
    return render(request, 'books/create.html',context)

def recently(num,category):
    recently_list=list()
    n=num.objects.all()

    for i in n:
        if book.was_published_recently(i)&book.category(i,category):
            recently_list.append(i)
    return recently_list
#starts here  ----
def another(request,pagename):

    if pagename=="about":
        return render(request,"books/about.html")
    elif pagename=="our_services":
        return render(request,"books/our_services.html")
    elif pagename=="contact_us":
        return render(request,"books/contact_us.html")

    else:
        context = {
            'all_books': book.objects.filter(book_category=pagename),
            "recently_list": recently(book,pagename),
            "category":pagename,
            'years_list':(years_collector()),

        }
        return render(request, 'books/category.html', context)


def thing(request,id):

        bk = get_object_or_404(book,id=id)
        from django.urls import reverse
        from django.shortcuts import render
        from paypal.standard.forms import PayPalPaymentsForm
        from django.contrib import messages
        from django.conf import settings
        host = request.get_host()
        # What you want the button to do.
        paypal_dict = {
                "business":settings.PAYPAL_RECEIVER_EMAIL,
                "amount":bk.book_price,
                "item_name":bk.book_name,
                'currency_code': 'USD',
                "invoice": bk.id,
                'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host,reverse('payment_done',args=[bk.id])),
                'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
                "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
            }

            # Create the instance.
        form = PayPalPaymentsForm(initial=paypal_dict)

        context = {
            "form": form,
            'book_name': bk.book_name,
            'book_describtion': bk.book_describtion,
            'book_photo': bk.book_photo,
            'pub_date': bk.pub_date,
            'file': bk.file,
            'book_price': bk.book_price,

            'all_books': book.objects.all(),
            'category': bk.book_category,
        }
        return render(request,'books/info.html',context)





def counter(num):
    x=0
    n=num.objects.all()
    for i in n:
        if book.was_published_recently(i):

            x+=1
    return x

def home(request):

    context={
        'all_books':book.objects.all(),
        'newest_books':counter(book),
        'years_list':(years_collector()),
        'now':timezone.now().strftime("%Y")
    }
    return render(request,'books/home.html',context,)

def about(request):

    return HttpResponse("hello")

def our_services(request):

    return render(request,'books/our_services.html')

def contact_us(request):

    return render(request,'books/contact_us.html')




# ...


def process_payment(request):
     pass






from django.views.generic import TemplateView, ListView
from django.db.models import Q
class HomePageView(TemplateView):
    template_name = 'books/search.html'
class SearchResultsView(ListView):
            model = book
            template_name = 'books/search_result.html'

            def get_queryset(self):  # new
                query = self.request.GET.get('q')
                object_list = book.objects.filter(
                    Q(book_name__icontains=query) | Q(book_category__icontains=query)
                )
                return object_list
