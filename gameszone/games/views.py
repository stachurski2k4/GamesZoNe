from django.shortcuts import render,redirect,get_object_or_404
from django.views  import generic
from . import models
from . import forms
from accounts import models as accounts_models
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class GamesList(generic.ListView):
    template_name='games_list.html'
    model=models.Game
    context_object_name='list'
class GameDetail(generic.DetailView):
    template_name='game_detail.html'
    model=models.Game
    context_object_name='game'
class GameAdd(LoginRequiredMixin,generic.CreateView):
    model=models.Game
    template_name='game_add.html'
    form_class=forms.GameForm

class EditGame(LoginRequiredMixin,generic.UpdateView):
    model=models.Game
    template_name='game_add.html'
    form_class=forms.GameForm
class DeleteGame(LoginRequiredMixin,generic.DeleteView):
    model=models.Game 
    success_url=reverse_lazy('games:list')
    template_name='confirm_delete.html'

@login_required
def addComment(request,pk):
    game=get_object_or_404(models.Game,pk=pk)
    _user=get_object_or_404(accounts_models.User,pk=request.user.pk)
    if(request.method=="POST"):
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.game=game
            comment.author=_user
            comment.save()
            return redirect('games:game',pk=pk)
    else:
        form=forms.CommentForm()
    return render(request,'comment_add.html',{'form':form,'pk':pk})

@login_required
def gameAdd(request):
    user=get_object_or_404(accounts_models.User,pk=request.user.pk)
    if(request.method=="POST"):
        form=forms.GameForm(request.POST,request.FILES)
        if form.is_valid():
            game=form.save(commit=False)
            game.author=user
            game.save()
            return redirect('games:game',pk=game.pk)
    else:
        form=forms.GameForm()
    return render(request,'game_add.html',{'form':form})

@login_required
def addVersion(request,pk):
    user=get_object_or_404(accounts_models.User,pk=request.user.pk)
    game=get_object_or_404(models.Game,pk=pk)
    if(request.method=="POST"):
        form=forms.VersionForm(request.POST,request.FILES)
        if form.is_valid():
            ver=form.save(commit=False)
            ver.author=user
            ver.game=game
            ver.save()
            return redirect('games:game',pk=pk)
    else:
        form=forms.VersionForm()
    return render(request,'version_add.html',{'form':form})

class DeleteVersion(LoginRequiredMixin,generic.DeleteView):
    model=models.Version 
    success_url=reverse_lazy('games:list')
    template_name='confirm_delete.html'

@login_required
def addImage(request,pk):
    game=get_object_or_404(models.Game,pk=pk)
    if(request.method=="POST"):
        form=forms.ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.game=game
            image.save()
            return redirect('games:game',pk=pk)
    else:
        form=forms.ImageForm()
    return render(request,'image_add.html',{'form':form,'pk':pk})