from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import RegistrationForm, UserProfileForm


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("successfully")
        else:
            if user_form.is_valid():
                return HttpResponse("userprofile_form is wrong")
            else:
                return HttpResponse("user_form is wrong.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    return render(request, "account/myself.html", {"user": user, "userprofile": userprofile})


@login_required(login_url='/account/login/')
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        userprofile_form = UserProfileForm(request.POST)
        if userprofile_form.is_valid():
            userprofile_cd = userprofile_form.cleaned_data
            userprofile.address = userprofile_cd['address']
            userprofile.aboutme = userprofile_cd['aboutme']
            userprofile.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        userprofile_form = UserProfileForm(
            initial={"sex": userprofile.sex, "address": userprofile.address, "aboutme": userprofile.aboutme})
        return render(request, "account/myself_edit.html",
                      {"userprofile": userprofile, "userprofile_form": userprofile_form})
