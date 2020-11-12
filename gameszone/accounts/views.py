from django.shortcuts import render,redirect,get_object_or_404
from django.views  import generic
from . import forms
from . import models
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate as auth_check,login
from django.contrib.auth.decorators import login_required
# Create your views here.

class ProfileView(generic.DetailView):
    model=models.User
    context_object_name='profile'
    template_name='profile_detail.html'
   
    # def get_queryset(self):
    #     queryset=super().get_queryset()
    #     return queryset.filter(username__iexact=self.kwargs.get('username'))
def signUp(request):
    registered=False

    if(request.method=='POST'):
        userForm=forms.UserForm(request.POST,request.FILES)
        if(userForm.is_valid()):
            user=userForm.save()
            user.save()
            registered=True
    else:
        userForm=forms.UserForm()
    return render(request,'signup.html',{'form':userForm,'registered':registered})

class EditProfile(generic.UpdateView):
    model=models.User
    template_name='profile_edit.html'
    form_class=forms.EditProfileForm

@login_required  
def editProfile(request,pk):
    _user=get_object_or_404(models.User,pk=pk)
    errors={}
    if(request.method=='POST'):
        userForm=forms.EditProfileForm(request.POST,request.FILES,instance=_user)
        if(userForm.is_valid()):
            if check_password(userForm.cleaned_data['password2'],_user.password):
                new_user=userForm.save()
                new_user.save()
                edited_user=auth_check(request,username=new_user.username,password=userForm.cleaned_data['password2'])
                if(edited_user):
                    login(request,edited_user)
                    return redirect('accounts:profile',pk=pk)
                else:
                    redirect('accounts:login')
            else:
                errors['pass_error']='Invalid Password!'
        else:
            errors['form_error']='Incorect data!'
    else:
        userForm=forms.EditProfileForm(instance=_user)
    return render(request,'profile_edit.html',{'pk': pk,'form':userForm,'errors':errors})
@login_required
def editPass(request,pk):
    errors={}
    _user=get_object_or_404(models.User,pk=pk)
    if request.method=="POST":
        passform=forms.EditPassForm(request.POST,request.FILES)
        if passform.is_valid():
            if check_password(passform.cleaned_data['password'],_user.password):
                if(passform.cleaned_data['password1']==passform.cleaned_data['password2']):
                    _user.password=make_password(passform.cleaned_data['password1'])
                    _user.save()
                    edited_user=auth_check(request,username=_user.username,password=passform.cleaned_data['password1'])
                    if(edited_user):
                        login(request,edited_user)
                        return redirect('accounts:profile',pk=pk)
                    else:
                        redirect('accounts:login')
                else:
                    errors['pass_error']='Passwords Do not Match!'
            else:
                errors['pass_error']='Invalid Password!'

    else:
        passform=forms.EditPassForm()
    return render(request,'pass_edit.html',{'errors':errors,'form':passform})


class ProfileList(generic.ListView):
    model=models.User
    template_name='profile_list.html'
    context_object_name='list'

class EditLevel(generic.UpdateView):
    model=models.User
    template_name='pass_edit.html'
    form_class=forms.EditLevelForm