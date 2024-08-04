from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from users.forms import UserCreateForm


# Create your views here.


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form,
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            
            return redirect('users:login')
        else:
            context = {
                "form": create_form, 
                "error": "Form is not valid."
                }
            
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")
