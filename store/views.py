from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import *
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator=Paginator(products, 6)
        page= request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator=Paginator(products, 6)
        page= request.GET.get('page')
        paged_products = paginator.get_page(page) #6 products will be shown in the first page
        product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart= CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e
    product_gallery = ProductGallery.objects.filter(product_id=single_product)
    context ={
        'single_product':single_product,
        'in_cart':in_cart,
        'product_gallery':product_gallery,
    }
    
    return render(request, 'store/product_detail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count=products.count()
    context={
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'store/store.html',context)

# from django.shortcuts import render, redirect
# from .forms import ContactForm

# def contact(request):
#     message_sent = False  # Initially set to False

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             message_sent = True  # Set to True after successful form submission
#             # You can also redirect to the success page if needed
#             # return redirect('success_page')
#     else:
#         form = ContactForm()

#     return render(request, 'store/contact.html', {'form': form, 'message_sent': message_sent})

from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Your message has been sent successfully!"
            form = ContactForm()  # Resetting the form for a new submission
    else:
        form = ContactForm()
        success_message = None
    
    return render(request, 'store/contact.html', {'form': form, 'success_message': success_message})
def faq(request):
    # Add any necessary context data here
    return render(request, 'store/faq.html')

def about(request):
    return render(request, 'store/about.html')