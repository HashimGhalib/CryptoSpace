from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from .forms import UserRegristrationForm


class Home(TemplateView):
    template_name = 'finexo-html/index.html'


class About(TemplateView):
    template_name = 'finexo-html/about.html'


class Team(TemplateView):
    template_name = 'finexo-html/team.html'


class Service(TemplateView):
    template_name = 'finexo-html/service.html'


class Why(TemplateView):
    template_name = 'finexo-html/why.html'


class SignUp(View):

    def get(self, request):
        form = UserRegristrationForm()
        return render(request, 'finexo-html/page-reg-page.html', {'form': form})

    def post(self, request):
        form = UserRegristrationForm(request.form)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['[password1']
                )

            login(request, user)
            return redirect('home')
        return render(request, 'finexo-html/page-reg-page.html', {'form': form})
