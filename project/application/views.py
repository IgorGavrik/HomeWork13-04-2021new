from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        context = {
            'title': "Home page",
        }
        return render(request, 'home.html', context)
