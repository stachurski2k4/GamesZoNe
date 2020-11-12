from django.views  import generic
from django.shortcuts import render
from games import models

def homePage(request):
    latest_games=models.Game.objects.order_by('-pk')[:4]
    popular_games=models.Game.objects.order_by('-downloads_count')[:4]
    return render(request,'index.html',{'latest_games':latest_games,'popular_games':popular_games})
class HomePage(generic.TemplateView):
    template_name='index.html'
class ThanksView(generic.TemplateView):
    template_name='thanks.html'
class InfoView(generic.TemplateView):
    template_name='info.html'