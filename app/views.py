from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
import stripe
stripe.api_key = 'Secret key'
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def charge(request):
    
    if request.method == 'POST':
        print('DATA:', request.POST)
        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['username'],
            source=request.POST['stripeToken']
            )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description='Donation'
        )
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    context = {'amount':amount}
    return render(request, 'app/success.html', context)