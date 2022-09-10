from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from.models import products,category
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def home(request):
    return render(request,'index.html')


def store(request,category_slug=None):
    cat = category.objects.all()
    categories=None
    product=None
    if category_slug != None:
        categories = get_object_or_404(category,slug=category_slug)
        product = products.objects.all().filter(categ= categories,available=True)
        paginator =  Paginator(product,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        product = products.objects.all().filter(available=True)
        paginator =  Paginator(product,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
    return render(request,'store.html',{'pr':paged_products,'cr':cat})


def product_detail(request,category_slug,product_slug):
    try:
        single_product = products.objects.get(categ__slug = category_slug,slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request,'detail.html',context)


def search(request):
    product = None
    if 'keyword' in request .GET:
        keyword = request.GET['keyword']
        if keyword:
            product = products.objects.filter(Q(name__contains=keyword)|Q(desc__contains=keyword)|Q(slug__contains=keyword))
    
    context = {
        'product':product
    }
    return render(request,'search.html',context)
 