from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Order
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import ConnextionForm

# Create your views here.
def index(request):
    product = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != "" and item_name is not None:
        product = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product, 4)
    page = request.GET.get("page")
    product = paginator.get_page(page)
    return render(request, "shop/index.html", {"products":product})

def detail(request, myid):
    product = Product.objects.get(id=myid)
    return render(request, "shop/detail.html", {"product":product})

User = get_user_model()
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        #login(request, user)    
        return redirect("login")
    return render(request, "accounts/register.html")

def connexion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("index")
    return render(request, "accounts/login.html")

def deconnexion(request):
    logout(request)
    return redirect("index")

def add_to_cart(request, myid):
    user = request.user
    product = get_object_or_404(Product, id=myid)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product, ordered=False)
    
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
        
    return redirect("index")

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "shop/cart.html", {"orders":cart.orders.all()})

def delete(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect("index")

def avertissement(request):
    return render(request, "shop/create_account.html")