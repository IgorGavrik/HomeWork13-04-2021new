from django.shortcuts import render
from django.views import View

from application.form import WriteLineForm
from application.models import Customer


class MainView(View):

    def get(self, request):
        context = {
            'form': WriteLineForm(),
            'title': "Форма для ввода данных",
        }
        return render(request, 'form.html', context)

    def post(self, request):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                firstname=form.cleaned_data.get('firstname'),
                lastname=form.cleaned_data.get('lastname'),
                age=form.cleaned_data.get('age'),
                comment=form.cleaned_data.get('comment'),
            )
            context = {
                'form': WriteLineForm(),
                'title': "Форма для ввода данных",
            }
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            age = form.cleaned_data.get('age')
            comment = form.cleaned_data.get('comment')
            print(f'{firstname} | {lastname} | {age} | {comment}')
        return render(request, "home.html", context)
