from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from store.models import  Product,Categories,Filter_Price,contact_us,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages


def Main(request):
     product = Product.objects.filter(status='PUBLISH')

     context ={
         'product': product,
     }
     return render(request,'index.html', context)



def CartPage(request):
    return render(request,'cart.html')


def CheckoutPage(request):
    return render(request,'checkout.html')

def ContactPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contact=contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return redirect('HomePage')

    return render(request,'contact.html')

def AboutPage(request):
    return render(request,'about.html')

def AccountPage(request):
    return render(request,'my-account.html')

def ChangePass(request):
    return render(request,'ChangePass.html')

def PRODUCT(request):
    # product = Product.objects.filter(status='PUBLISH')
    categories=Categories.objects.all()
    filter_price=Filter_Price.objects.all()
    CATID=request.GET.get('categories')
    Filter_Price_id=request.GET.get('filter_price')

    if CATID:
        product=Product.objects.filter(categories=CATID,status='PUBLISH')
    elif Filter_Price_id:
        product=Product.objects.filter(filter_price=Filter_Price_id,status='PUBLISH')
    else:
        product=Product.objects.filter(status='PUBLISH')

    context ={
         'product': product,
         'categories':categories,
        #  'subcategories':subcategories,
         'filter_price':filter_price,
     }

    return render(request,'shop-left-sidebar.html',context)

def DetailsPage(request,id):
    prod=Product.objects.filter(id = id ).first()
    context={
         'prod': prod,
    }
    return render(request,'single-product.html',context)


def RegisterPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')

        if password != confirm_password:
            messages.success(request, "Mismatch Password")
            # return render(request, 'auth.html', {'error': 'Passwords do not match'})

        # Create user
        customer = User.objects.create_user(username=username, email=email, password=password)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        
        # Assuming you have a UserProfile model to store additional information
        # Replace UserProfile with the actual name of your profile model
        # Create user profile
        user_profile = UserProfile.objects.create(user=customer, gender=gender, mobile_no=mobile_no, address=address)
        

        return redirect('LoginPage')

    return render(request,'Register.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HomePage')  # Redirect to the home page upon successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        # Check if the user is already authenticated
        # if request.user.is_authenticated:
        #     return redirect('HomePage')  # Redirect to the home page if the user is already authenticated
        # else:
            return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/Login/')

