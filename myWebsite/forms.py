from django.forms import ModelForm
from .models import Testimonial, Contact, PreviousProjects, MyServices


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PreviousProjectsForm(ModelForm):
    class Meta:
        model = PreviousProjects
        fields = '__all__'


class MyServicesForm(ModelForm):
    class Meta:
        model = MyServices
        fields = '__all__'

