from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, CreateView
from django.contrib.auth import get_user_model
from .forms import ContactForm
from django.contrib import messages

# def index(request):
#     return render(request, 'index.html')

# class IndexView(View):
#     def get(self, request):
#         return render(request, 'index.html')

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
        # messages.success(request, 'Mensagem enviada com sucesso!')
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
