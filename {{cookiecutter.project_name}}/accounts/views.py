from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserCreationForm, UserSettingsForm


class UserSettings(LoginRequiredMixin, View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        form = UserSettingsForm(
            initial={
                k: v
                for k in ("id", "username", "email", "first_name", "last_name")
                if (v := getattr(request.user, k))
            }
        )
        return render(request, "accounts/user_settings.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserSettingsForm(request.POST.dict(), instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("categories:list")
        print(form.errors)
        return redirect("home")


class UserRegistration(View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(
            request, "registration/user_registration.html", {"register_form": form}
        )

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            get_user_model().objects.create_user_profile(user)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("categories:list")
        messages.add_message(
            request, messages.ERROR, "Unsuccessful registration. Invalid information."
        )
        return redirect("user-register")
