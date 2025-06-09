from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "pages/homepage.html")


## CBV version
# class HomePageView(TemplateView):
#     template_name = 'pages/homepage.html'

