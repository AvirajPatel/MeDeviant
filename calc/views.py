from django.shortcuts import render
from .models import medicine

# Create your views here.

def index(request):

    med1 = medicine()
    med1.name = 'Mask | 100pcs'
    med1.price = '₹300.00'
    med1.img = 'c1.jpg'
    
    med2 = medicine()
    med2.name = 'Dettol Hand Sanitizer | 200ml'
    med2.price = '₹100.00'
    med2.img = 'c2.jpg'
    
    med3 = medicine()
    med3.name = 'Dettol Handwash | 300ml'
    med3.price = '₹150.00'
    med3.img = 'c3.jpg'

    med4 = medicine()
    med4.name = 'PPE Kit'
    med4.price = '₹500.00'
    med4.img = 'c4.jpg'

    med5 = medicine()
    med5.name = 'Chyawanprash'
    med5.price = '₹400.00'
    med5.img = 'wc1.jpg'
    
    med6 = medicine()
    med6.name = 'Vicks VapoRub'
    med6.price = '₹80.00'
    med6.img = 'wc2.jpg'
    
    med7 = medicine()
    med7.name = 'Dove Men Care | Antidandruff Shampoo'
    med7.price = '₹250.00'
    med7.img = 'wc4.jpg'

    med8 = medicine()
    med8.name = 'Vicks Cough Syrup | Honey Flavour'
    med8.price = '₹110.00'
    med8.img = 'wc5.jpg'



    meds = [med8, med2, med3, med4, med5, med6, med7, med1]
    
    return render(request, 'index.html', {'meds' : meds})

def products(request):

    med1 = medicine()
    med1.name = 'Mask | 100pcs'
    med1.price = '₹300.00'
    med1.img = 'c1.jpg'
    
    med2 = medicine()
    med2.name = 'Dettol Hand Sanitizer | 200ml'
    med2.price = '₹100.00'
    med2.img = 'c2.jpg'
    
    med3 = medicine()
    med3.name = 'Dettol Handwash | 300ml'
    med3.price = '₹150.00'
    med3.img = 'c3.jpg'

    med4 = medicine()
    med4.name = 'PPE Kit'
    med4.price = '₹500.00'
    med4.img = 'c4.jpg'

    med5 = medicine()
    med5.name = 'Chyawanprash'
    med5.price = '₹400.00'
    med5.img = 'wc1.jpg'
    
    med6 = medicine()
    med6.name = 'Vicks VapoRub'
    med6.price = '₹80.00'
    med6.img = 'wc2.jpg'
    
    med7 = medicine()
    med7.name = 'Dove Men Care | Antidandruff Shampoo'
    med7.price = '₹250.00'
    med7.img = 'wc4.jpg'

    med8 = medicine()
    med8.name = 'Vicks Cough Syrup | Honey Flavour'
    med8.price = '₹110.00'
    med8.img = 'wc5.jpg'



    meds = [med8, med2, med3, med4, med5, med6, med7, med1]

    return render(request, 'products.html', {'meds' : meds})

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')