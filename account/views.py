from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileUpdateForm, UserProfileForm
from .models import UserProfile


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect("login")

    else:
        form = RegisterForm()

    templ = "account/register.html"
    data = {"form": form}

    return render(request, templ, data)


@login_required
def profile(request):
    templ = "account/profile.html"
    return render(request, templ)


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = ProfileUpdateForm(
            request.POST,
            instance=request.user,
        )
        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    templ = "account/profile_edit.html"
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, templ, context)
