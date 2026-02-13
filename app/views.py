from django.shortcuts import render
from django.http import HttpResponse

from .forms import *

# Create your views here.
def contact(request):
    ECFO = ContactForm()
    d = {'ECFO': ECFO}

    if request.method == 'POST':
        LFDO = ContactForm(request.POST)
        if LFDO.is_valid():
            data = LFDO.cleaned_data
            return HttpResponse(f"""
                Name: {data['name']} <br>
                Email: {data['email']} <br>
                Age: {data['age']} <br>
                Message: {data['message']}
            """)
        else:
            return HttpResponse('Form is not valid')

    return render(request, 'contact.html', d)


        