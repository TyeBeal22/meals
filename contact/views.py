from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.contrib import messages
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import ContactForm
from .models import Order
import random

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try : 
                send_mail(subject,message,from_email,['dangdatsdelicious@gmail.com'])

            except BadHeaderError:
                return HttpResponse('ivalid header') 

            return redirect('contact:send_success')
    

    else:
        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request , 'contact/contact.html' , context)



def send_success(request):
    return HttpResponse('thanks you for your email ^_^')


def order(request):
      
  ref_num = 0  
  if request.method == 'POST':
    meal_id = request.POST['meal_id']
    meal = request.POST['meal']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    guests = request.POST['guests']    
    message = request.POST['message']
    delivery_address = request.POST['delivery_address']
    event_date = request.POST['event_date']
    #is_delivery = request.POST['is_delivery']
    #  Check if user has made inquiry already
    #if request.user.is_authenticated:
      #user_id = request.user.id
      #has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      #if has_contacted:
        #messages.error(request, 'You have already placed an order for this item')
        #return redirect('/listings/'+listing_id)

    order = Order(meal=meal, meal_id=meal_id, name=name, email=email, phone=phone, message=message, guests=guests, delivery_address=delivery_address,event_date=event_date)

    order.save()
    ref_num = random.randint(1,500)
    # Send email
        
    send_mail(
           'Dang Dats Delicious Order',
            'There has been an order for ' + meal + '. By Customer ' + name + '. Your Order # is ' + str(ref_num) + '. Thank you for shopping with DangDatsDelicious',
           'darthtye@gmail.com',
           ['dangdatsdelicious@gmail.com',email],
           fail_silently=False
         )

    messages.success(request, 'Your order has been submitted!')
    return redirect('/meals/'+meal_id)
