from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView

from .forms import ContactForm


# def index(request):
#     return render(request, 'index.html')

# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
