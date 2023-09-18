from django.http import HttpResponseRedirect
from django.shortcuts import render 
from website.forms import ContactForm , NewsletterForm 
from django.contrib import messages

def index(request):
    return render(request,'index.html')


    
#Form of contact us!

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS, 'Successfull !') #success message
            #return JsonResponse({'success': True})
        else:           
            messages.add_message(request,messages.ERROR, 'ERROR! Try again carefully!') #error message
            #return JsonResponse({'success': False})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form} )



def about(request):
    return render(request,'about.html')


#Form of Newsletter!! after Enter Ur email we save it and return you back to home.html !!
from django.contrib import messages
from django.http import HttpResponseRedirect

def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return HttpResponseRedirect("/")
        else:
            # Add an error message
            messages.error(request, 'There was an error with your submission. Please try again.')
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


# 404 and 500 handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)