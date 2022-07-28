from django.shortcuts import render
from .models import *
"""
smtp / send messages
PreviousProjects
Testimonial
MyServices
Contact
"""


def test(request):
    previousProjects = PreviousProjects.objects.all()
    testimonial = Testimonial.objects.all()
    myServices = MyServices.objects.all()
    contact = Contact.objects.all()

    context = {
        'previousProjects':previousProjects,
        'testimonial': testimonial,
        'myServices': myServices,
        'contact': contact,
    }
    return render(request, 'myWebsite/index.html', context)
